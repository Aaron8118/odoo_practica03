# from odoo import http


# class RpgPersonatges(http.Controller):
#     @http.route('/rpg_personatges/rpg_personatges', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rpg_personatges/rpg_personatges/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rpg_personatges.listing', {
#             'root': '/rpg_personatges/rpg_personatges',
#             'objects': http.request.env['rpg_personatges.rpg_personatges'].search([]),
#         })

#     @http.route('/rpg_personatges/rpg_personatges/objects/<model("rpg_personatges.rpg_personatges"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rpg_personatges.object', {
#             'object': obj
#         })

