from odoo import models, fields, api

from odoo import models, fields, api
from datetime import timedelta
from markupsafe import escape


class Esdeveniment(models.Model):
    _name = 'venda_entrades_segures.esdeveniment'
    _description = 'Esdeveniment'

    name = fields.Char(
        string='Nom de l esdeveniment',
        required=True
    )

    preu_base = fields.Float(
        string='Preu base',
        required=True
    )
    
    data_inici = fields.Datetime(
        string='Data d inici'
    )


class Etiqueta(models.Model):
    _name = 'venda_entrades_segures.etiqueta'
    _description = 'Etiqueta'

    name = fields.Char(
        string='Nom de l etiqueta',
        required=True
    )


class Tiquet(models.Model):
    _name = 'venda_entrades_segures.tiquet'
    _description = 'Tiquet de venda'


    comprador_id = fields.Many2one(
        'res.partner',
        string='Comprador',
        required=True
    )

    esdeveniment_id = fields.Many2one(
        'venda_entrades_segures.esdeveniment',
        string='Esdeveniment',
        required=True
    )

    preu_final = fields.Float(
        string='Preu final',
        compute='_compute_preu_final',
        store=True
    )

    @api.depends('esdeveniment_id.preu_base')
    def _compute_preu_final(self):
        for record in self:
            if record.esdeveniment_id:
                record.preu_final = (
                    record.esdeveniment_id.preu_base * 1.10
                )
            else:
                record.preu_final = 0.0

    codi_seguretat = fields.Char(
        string='Codi de seguretat',
        compute='_compute_codi_seguretat',
        store=True
    )
    
    @api.depends('comprador_id.name', 'esdeveniment_id')
    def _compute_codi_seguretat(self):
        for record in self:
            if record.comprador_id and record.esdeveniment_id:
                nom = record.comprador_id.name.upper().replace(' ', '-')
                record.codi_seguretat = (
                    f"{nom}-{record.esdeveniment_id.id}-{record.id or 0}"
                )
            else:
                record.codi_seguretat = False


    data_limit_acces = fields.Datetime(
        string='Data limit d acces',
        compute='_compute_data_limit_acces',
        store=True
    )
    
    @api.depends('esdeveniment_id.data_inici')
    def _compute_data_limit_acces(self):
        for record in self:
            if record.esdeveniment_id and record.esdeveniment_id.data_inici:
                data_inici = fields.Datetime.to_datetime(
                    record.esdeveniment_id.data_inici
                )
                record.data_limit_acces = (
                    data_inici - timedelta(hours=2)
                )
            else:
                record.data_limit_acces = False


    foto_comprador = fields.Image(
        string='Foto del comprador',
        compute='_compute_foto_comprador',
        store=True
    )

    @api.depends('comprador_id.image_1920')
    def _compute_foto_comprador(self):
        for record in self:
            record.foto_comprador = record.comprador_id.image_1920


    clausules_legals = fields.Html(
        string='Clausules legals',
        compute='_compute_clausules_legals',
        store=True
    )
    
    @api.depends('comprador_id.name')
    def _compute_clausules_legals(self):
        for record in self:
            if record.comprador_id:
                nom = record.comprador_id.name
    
                record.clausules_legals = (
                    '<p>Comprador: <strong>' + nom + '</strong></p>'
                    '<p>Entrada nominal i intransferible.</p>'
                    '<p>Prohibida la revenda.</p>'
                    '<p>No es permet el reemborsament.</p>'
                )
            else:
                record.clausules_legals = False

    @api.model
    def _get_default_tags(self):
        nominal = self.env.ref(
            'venda_entrades_segures.etiqueta_nominal'
        )
    
        no_reemborsable = self.env.ref(
            'venda_entrades_segures.etiqueta_no_reemborsable'
        )
    
        return [(6, 0, (nominal | no_reemborsable).ids)]
        
    etiquetes_ids = fields.Many2many(
        'venda_entrades_segures.etiqueta',
        'tiquet_etiqueta_rel',
        'tiquet_id',
        'etiqueta_id',
        string='Etiquetes',
        default=_get_default_tags
    )

    entrades_relacionades_ids = fields.Many2many(
        'venda_entrades_segures.tiquet',
        string='Entrades relacionades',
        compute='_compute_entrades_relacionades'
    )

    @api.depends('comprador_id', 'esdeveniment_id')
    def _compute_entrades_relacionades(self):
        for record in self:
            if record.id:
                domain = [
                    ('id', '!=', record.id),
                    '|',
                    ('comprador_id', '=', record.comprador_id.id),
                    ('esdeveniment_id', '=', record.esdeveniment_id.id)
                ]

                record.entrades_relacionades_ids = self.search(domain)
            else:
                record.entrades_relacionades_ids = False

def crear_etiquetes(env):
    Etiqueta = env['venda_entrades_segures.etiqueta']

    if not Etiqueta.search([('name', '=', 'Nominal')], limit=1):
        Etiqueta.create({'name': 'Nominal'})

    if not Etiqueta.search([('name', '=', 'No Reemborsable')], limit=1):
        Etiqueta.create({'name': 'No Reemborsable'})


