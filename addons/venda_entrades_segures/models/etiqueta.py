from odoo import models, fields


class Etiqueta(models.Model):
    _name = 'venda_entrades_segures.etiqueta'
    _description = 'Etiqueta de les entrades'

    name = fields.Char(
        string='Nom',
        required=True
    )

    descripcio = fields.Text(
        string='Descripció'
    )
