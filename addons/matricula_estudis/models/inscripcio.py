
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Inscripcio(models.Model):
    _name = 'matricula.inscripcio'
    _description = 'Inscripcio'

    alumne_id = fields.Many2one(
        'matricula.alumne',
        string='Alumne',
        required=True,
        domain="[('id', 'in', alumne_elegible_ids)]"
    )

    curs_id = fields.Many2one(
        'matricula.curs',
        string='Curs',
        required=True
    )

    data_inscripcio = fields.Date(
        string='Data d inscripcio',
        required=True
    )

    alumne_elegible_ids = fields.Many2many(
        'matricula.alumne',
        string='Alumnes elegibles',
        compute='_compute_alumne_elegible_ids',
        store=False
    )

    @api.depends(
        'curs_id',
        'curs_id.edat_minima',
        'curs_id.inscripcio_ids.alumne_id',
        'alumne_id'
    )
    def _compute_alumne_elegible_ids(self):
        Alumne = self.env['matricula.alumne']
        Inscripcio = self.env['matricula.inscripcio']

        for record in self:
            if not record.curs_id:
                record.alumne_elegible_ids = Alumne.browse([])
                continue

            matriculats = Inscripcio.search([
                ('curs_id', '=', record.curs_id.id),
                ('id', '!=', record.id or 0)
            ]).mapped('alumne_id').ids

            alumnes = Alumne.search([
                ('edat', '>=', record.curs_id.edat_minima),
                ('id', 'not in', matriculats)
            ])

            record.alumne_elegible_ids = alumnes

    @api.constrains('data_inscripcio', 'curs_id')
    def _check_data_inscripcio(self):
        for record in self:
            if record.curs_id and record.data_inscripcio:
                if (
                    record.data_inscripcio < record.curs_id.data_inici
                    or record.data_inscripcio > record.curs_id.data_fi
                ):
                    raise ValidationError(
                        'La data d inscripcio ha d estar dins del periode del curs.'
                    )

    @api.constrains('alumne_id', 'curs_id')
    def _check_edat_alumne(self):
        for record in self:
            if record.alumne_id and record.curs_id:
                if record.alumne_id.edat < record.curs_id.edat_minima:
                    raise ValidationError(
                        'L alumne no compleix l edat mínima del curs.'
                    )

    @api.constrains('curs_id')
    def _check_capacitat(self):
        for record in self:
            if record.curs_id:
                total = self.search_count([
                    ('curs_id', '=', record.curs_id.id)
                ])

                if total > record.curs_id.capacitat_maxima:
                    raise ValidationError(
                        'El curs ja ha arribat a la seva capacitat màxima.'
                    )
