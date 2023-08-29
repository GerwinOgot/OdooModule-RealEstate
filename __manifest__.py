# -*- coding: utf-8 -*-
{
    'name': "Real_Estate",

    'summary': """
        Real Estate App""",

    'description': """
        Selling Houses
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_model_views.xml',
        'views/views.xml',
        'views/templates.xml',
        'report/report.xml',
        'report/estate_report.xml'


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
