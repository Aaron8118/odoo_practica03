from odoo import models, fields


class BasquetEquip(models.Model):
    _name = 'basquet.equip'
    _description = 'Equip de basquet'

    name = fields.Char(string='Nom de l equip', required=True)
    ciutat = fields.Char(string='Ciutat')

    jugador_ids = fields.One2many(
        'basquet.jugador',
        'equip_id',
        string='Jugadors'
    )

    estadi_id = fields.Many2one(
        'basquet.pavello',
        string='Estadi principal',
        domain="[('ciutat', '=', ciutat)]"
    )

    equips_agermanats_ids = fields.Many2many(
        'basquet.equip',
        'basquet_equip_agermanats_rel',
        'equip_id',
        'agermanat_id',
        string='Equips agermanats'
    )

    equips_rivals_ids = fields.Many2many(
        'basquet.equip',
        'basquet_equip_rivals_rel',
        'equip_id',
        'rival_id',
        string='Equips rivals'
    )

class BasquetJugador(models.Model):
    _name = 'basquet.jugador'
    _description = 'Jugador de basquet'

    name = fields.Char(string='Nom del jugador', required=True)

    equip_id = fields.Many2one(
        'basquet.equip',
        string='Equip',
        domain="[('estadi_id', '!=', False)]"
    )

    estadi_nom = fields.Char(
	string='Nom de l estadi',
        store=True,
        readonly=True,
	related='equip_id.estadi_id.name'
    )

    es_capita = fields.Boolean(
        string='Es capita',
        default=False
    )

class BasquetPavello(models.Model):
    _name = 'basquet.pavello'
    _description = 'Pavello de basquet'

    name = fields.Char(
        string='Nom del pavello',
        required=True
    )

    ciutat = fields.Char(
        string='Ciutat'
    )
