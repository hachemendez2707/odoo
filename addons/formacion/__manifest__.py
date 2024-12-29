# -*- coding: utf-8 -*-
{
    'name': 'Formación Interna',
    'summary': 'Gestión de cursos y formadores para la formación continua de la empresa.',
    'description': 'Este módulo gestiona las acciones formativas, incluyendo cursos, formadores, y participantes.',

    'author': "Hillary Méndez",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '1.5',

    # any module necessary for this one to work correctly
    'depends': ['hr', 'contacts', 'base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/formacion_views.xml',
        'views/empleados_views.xml',
        'views/proveedores_views.xml',
        'views/menu_items.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',  # Añadido para evitar el warning
}

