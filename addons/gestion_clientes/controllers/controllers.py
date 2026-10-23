# from odoo import http


# class GestionClientes(http.Controller):
#     @http.route('/gestion_clientes/gestion_clientes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_clientes/gestion_clientes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_clientes.listing', {
#             'root': '/gestion_clientes/gestion_clientes',
#             'objects': http.request.env['gestion_clientes.gestion_clientes'].search([]),
#         })

#     @http.route('/gestion_clientes/gestion_clientes/objects/<model("gestion_clientes.gestion_clientes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_clientes.object', {
#             'object': obj
#         })

