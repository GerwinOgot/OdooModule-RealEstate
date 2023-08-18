# -*- coding: utf-8 -*-
# from odoo import http


# class D:\projects-odoo\realestate(http.Controller):
#     @http.route('/d:\projects-odoo\realestate/d:\projects-odoo\realestate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/d:\projects-odoo\realestate/d:\projects-odoo\realestate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('d:\projects-odoo\realestate.listing', {
#             'root': '/d:\projects-odoo\realestate/d:\projects-odoo\realestate',
#             'objects': http.request.env['d:\projects-odoo\realestate.d:\projects-odoo\realestate'].search([]),
#         })

#     @http.route('/d:\projects-odoo\realestate/d:\projects-odoo\realestate/objects/<model("d:\projects-odoo\realestate.d:\projects-odoo\realestate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('d:\projects-odoo\realestate.object', {
#             'object': obj
#         })
