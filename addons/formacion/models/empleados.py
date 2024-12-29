from odoo import models, fields

class Empleados(models.Model):
    _inherit = 'hr.employee'

    formaciones_ids = fields.Many2many(
        'formacion.formacion',
        'employee_formacion_rel',  # Nombre de la tabla intermedia
        'employee_id',  # Campo en la tabla intermedia que se refiere a 'hr.employee'
        'formacion_id',  # Campo en la tabla intermedia que se refiere a 'formacion.formacion'
        string='Formaciones Internas')
