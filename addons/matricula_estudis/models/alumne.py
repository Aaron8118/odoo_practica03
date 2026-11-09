
from odoo import models, fields


class Alumne(models.Model):
    _name = 'matricula.alumne'
    _description = 'Alumne'

    name = fields.Char(
        string='Nom de l alumne',
        required=True
    )

    nif = fields.Char(
        string='NIF',
        required=True
    )

    edat = fields.Integer(
        string='Edat',
        required=True
    )

    _nif_unique = models.Constraint(
        'UNIQUE(nif)',
        'El NIF ha de ser únic.'
    )

    _edat_positiva = models.Constraint(
        'CHECK(edat > 0)',
        'L edat ha de ser positiva.'
    )

    inscripcio_ids = fields.One2many(
        'matricula.inscripcio',
        'alumne_id',
        string='Inscripcions'
    )
