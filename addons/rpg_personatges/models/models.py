# from odoo import models, fields, api


# class rpg_personatges(models.Model):
#     _name = 'rpg_personatges.rpg_personatges'
#     _description = 'rpg_personatges.rpg_personatges'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

