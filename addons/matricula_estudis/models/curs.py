
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Curs(models.Model):
    _name = 'matricula.curs'
    _description = 'Curs'

    name = fields.Char(string='Nom del curs', required=True)

    data_inici = fields.Date(
        string='Data d inici',
        required=True
    )

    data_fi = fields.Date(
        string='Data de fi',
        required=True
    )

    edat_minima = fields.Integer(
        string='Edat mínima',
        required=True
    )

    capacitat_maxima = fields.Integer(
        string='Capacitat màxima',
        required=True
    )

    inscripcio_ids = fields.One2many(
        'matricula.inscripcio',
        'curs_id',
        string='Inscripcions'
    )

    _sql_constraints = [
        (
            'capacitat_maxima_positiva',
            'CHECK(capacitat_maxima > 0)',
            'La capacitat màxima ha de ser superior a zero.'
        ),
    ]

    @api.constrains('data_inici', 'data_fi')
    def _check_dates(self):
        for record in self:
            if record.data_inici and record.data_fi:
                if record.data_fi < record.data_inici:
                    raise ValidationError(
                        'La data de fi no pot ser anterior a la data d inici.'
                    )
