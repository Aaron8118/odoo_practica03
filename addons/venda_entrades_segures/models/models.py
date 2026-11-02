# from odoo import models, fields, api


# class venda_entrades_segures(models.Model):
#     _name = 'venda_entrades_segures.venda_entrades_segures'
#     _description = 'venda_entrades_segures.venda_entrades_segures'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

