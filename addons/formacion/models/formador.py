from odoo import models, fields

class Formador(models.Model):
    _inherit = 'res.partner'

    es_formador = fields.Boolean(string='Es Formador', default=False)
    especialidad = fields.Char(string='Especialidad')
    formaciones_ids = fields.Many2many(
        'formacion.formacion',
        'formador_formacion_rel',  # Nombre de la tabla intermedia
        'formador_id',  # Campo en la tabla intermedia que se refiere a 'res.partner'
        'formacion_id',  # Campo en la tabla intermedia que se refiere a 'formacion.formacion'
        string='Formaciones Impartidas')
