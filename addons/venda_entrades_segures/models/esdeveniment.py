from odoo import models, fields


class Esdeveniment(models.Model):
    _name = 'venda_entrades_segures.esdeveniment'
    _description = 'Esdeveniment'

    name = fields.Char(
        string='Nom de l\'esdeveniment',
        required=True
    )

    preu_base = fields.Float(
        string='Preu base',
        required=True
    )

    data_inici = fields.Datetime(
        string='Data d\'inici',
        required=True,
        default=fields.Datetime.now
    )

    tiquet_ids = fields.One2many(
        'venda_entrades_segures.tiquet',
        'esdeveniment_id',
        string='Entrades'
    )
