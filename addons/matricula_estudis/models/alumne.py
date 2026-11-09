
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

    _sql_constraints = [
        (
            'nif_unique',
            'UNIQUE(nif)',
            'El NIF ha de ser únic.'
        ),
        (
            'edat_positiva',
            'CHECK(edat > 0)',
            'L edat ha de ser un número positiu.'
        ),
    ]

    inscripcio_ids = fields.One2many(
        'matricula.inscripcio',
        'alumne_id',
        string='Inscripcions'
    )
