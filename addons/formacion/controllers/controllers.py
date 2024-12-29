# -*- coding: utf-8 -*-
#from odoo import http


#class Formacion(http.Controller):
#    @http.route('/formacion/formacion', auth='public')
#    def index(self, **kw):
#         return "Hello, world"

#    @http.route('/formacion/formacion/objects', auth='public')
#    def list(self, **kw):
#         return http.request.render('formacion.listing', {
#             'root': '/formacion/formacion',
#             'objects': http.request.env['formacion.formacion'].search([]),
#         })

#    @http.route('/formacion/formacion/objects/<model("formacion.formacion"):obj>', auth='public')
#    def object(self, obj, **kw):
#         return http.request.render('formacion.object', {
#            'object': obj
#         })

