# from odoo import models, fields, api


# class matricula_estudis(models.Model):
#     _name = 'matricula_estudis.matricula_estudis'
#     _description = 'matricula_estudis.matricula_estudis'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

