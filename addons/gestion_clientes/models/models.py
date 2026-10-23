from odoo import models, fields, api


class gestion_clientes(models.Model):
    _name = 'gestion_clientes.gestion_clientes'
    _description = 'gestion_clientes.gestion_clientes'

    char = fields.Char(required=True)
    int = fields.Integer(required=True,default=0)
    text = fields.Text()
    float = fields.Float(default=0.0)
    bool = fields.Boolean()
    date =  fields.Date()
    date_time = fields.Datetime()
    html = fields.Html()
    img = fields.Image(max_width=512,max_height=512)
    selection = fields.Selection(selection=[('opcion1','opcion1'),('opcion2','opcion2'),('opcion3','opcion3')])

