# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': "Odoo Celery demo",

    'summary': "A dummy addon that launches tasks ran by Celery",
    'description': """Contains model OdooCeleryLauncher with a method bound to a button that launches 
a Task.""",

    'author': "Cyril MORISSE",
    'website': "http://twitter.com/cmorisse",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base'
    ],

    # always loaded
    'data': [
        'views/odoocelery_launcher.xml',
        'menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': True,
    'auto_install': False,
    'installable': True
}
