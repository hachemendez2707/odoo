from odoo import models, fields, api


class Formacion(models.Model):
    _name = 'formacion.formacion'
    _description = 'Formación Interna - Gestión de Cursos'

    nombre = fields.Char(string='Nombre del Curso', required=True)
    formador_id = fields.Many2one('res.partner', string='Formador', domain="[('es_formador', '=', True)]",
                                  required=True)
    participantes_ids = fields.Many2many('hr.employee', string='Participantes')
    duracion = fields.Float(string='Duración del Curso (horas)', required=True)
    horas_por_sesion = fields.Float(string='Horas por Sesión', required=True)
    numero_sesiones = fields.Integer(string='Número de Sesiones', compute='_compute_numero_sesiones', store=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha de Fin', compute='_compute_fecha_fin', store=True)
    descripcion = fields.Text(string='Descripción del Curso')

    @api.depends('duracion', 'horas_por_sesion')
    def _compute_numero_sesiones(self):
        for record in self:
            record.numero_sesiones = int(record.duracion / record.horas_por_sesion) if record.horas_por_sesion else 0

    @api.depends('fecha_inicio', 'numero_sesiones')
    def _compute_fecha_fin(self):
        for record in self:
            if record.fecha_inicio and record.numero_sesiones:
                record.fecha_fin = fields.Date.add(record.fecha_inicio, days=(record.numero_sesiones - 1))
            else:
                record.fecha_fin = False
