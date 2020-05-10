# -*- coding: utf-8 -*-
{
    'name': "myFirstModule",

    'summary': """
        Manage library""",

    'description': """
        Manage library book catalogue and lending
    """,

    'author': "Maud_Pixel",
    'website': "http://www.maud-pixel.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'application': True,
    'data': ['security/library_security.xml',
             'security/ir.model.access.csv',
             'views/library_menu.xml']
}
