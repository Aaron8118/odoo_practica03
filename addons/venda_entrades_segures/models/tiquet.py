from odoo import models, fields, api
from datetime import timedelta
from markupsafe import escape


class Tiquet(models.Model):
    _name = 'venda_entrades_segures.tiquet'
    _description = 'Tiquet nominal'
    name = fields.Char(string="Nom del tiquet", required=True)

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

    @api.depends(
        'comprador_id.name',
        'esdeveniment_id'
    )
    def _compute_codi_seguretat(self):
        for record in self:
            nom = record.comprador_id.name or 'SENSE_NOM'
            esdeveniment = record.esdeveniment_id.id or 0
            tiquet = record.id or 0
    
            record.codi_seguretat = (
                f"{record.comprador_id.name}-"
                f"{record.esdeveniment_id.id}"
            )


    data_limit_acces = fields.Datetime(
        string='Data límit d\'accés',
        compute='_compute_data_limit_acces',
        store=True
    )

    @api.depends('esdeveniment_id.data_inici')
    def _compute_data_limit_acces(self):
        for record in self:
            if record.esdeveniment_id.data_inici:
                record.data_limit_acces = (
                    record.esdeveniment_id.data_inici
                    - timedelta(hours=2)
                )
            else:
                record.data_limit_acces = False



    foto_comprador = fields.Image(
        string='Foto del comprador',
        compute='_compute_foto_comprador'
    )

    @api.depends('comprador_id.image_1920')
    def _compute_foto_comprador(self):
        for record in self:
            record.foto_comprador = (
                record.comprador_id.image_1920
                if record.comprador_id
                else False
            )



    clausules_legals = fields.Html(
        string='Clàusules legals',
        compute='_compute_clausules_legals'
    )

    @api.depends('comprador_id.name')
    def _compute_clausules_legals(self):
        for record in self:
            nom = escape(
                record.comprador_id.name or 'Comprador'
            )

            record.clausules_legals = (
                f"<p>El comprador <strong>{nom}</strong> "
                "accepta les següents condicions:</p>"
                "<ul>"
                "<li>L'entrada és nominal i intransferible.</li>"
                "<li>Queda prohibida la revenda de l'entrada.</li>"
                "<li>No es permet el reemborsament.</li>"
                "</ul>"
            )


    etiquetes_ids = fields.Many2many(
    'venda_entrades_segures.etiqueta',
    'tiquet_etiqueta_rel',
    'tiquet_id',
    'etiqueta_id',
    string='Etiquetes',
    default=lambda self: self._get_default_tags()
)

    @api.model
    def _get_default_tags(self):
        etiqueta_nominal = self.env.ref(
            'venda_entrades_segures.etiqueta_nominal'
        )

        etiqueta_no_reemborsable = self.env.ref(
            'venda_entrades_segures.etiqueta_no_reemborsable'
        )

        return [
            (6, 0, [
                etiqueta_nominal.id,
                etiqueta_no_reemborsable.id
            ])
        ]



    entrades_relacionades_ids = fields.Many2many(
        'venda_entrades_segures.tiquet',
        'tiquet_relacionat_rel',
        'tiquet_id',
        'tiquet_relacionat_id',
        string='Entrades relacionades',
        compute='_compute_entrades_relacionades'
    )
    
    @api.depends(
        'comprador_id',
        'esdeveniment_id'
    )
    def _compute_entrades_relacionades(self):
        for record in self:
            if not record.id:
                record.entrades_relacionades_ids = False
                continue
    
            domain = [
                ('id', '!=', record.id),
                '|',
                ('esdeveniment_id', '=', record.esdeveniment_id.id),
                ('comprador_id', '=', record.comprador_id.id)
            ]
    
            record.entrades_relacionades_ids = self.search(domain)
