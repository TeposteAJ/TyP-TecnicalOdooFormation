# -*- coding: utf-8 -*-

{
    'name': 'Space Mision',
    'version': '1.0',
    'summary': """ Spacial Mision App to manage the mision to the space""",
    # 'description': """
    #     Library App to manage books and clients, that need help to rent books.
    #     - Clients
    #     -Books
    # """,
    'author': 'Angela Tesposte',
    'website': 'https://github.com/TeposteAJ',
    'license': 'GPL-3',
    'category': 'Training',
    'depends': ['base'],
    'data': [
        'security/spacial_mision_groups.xml',
        'security/spacial_mision_security.xml',
        'security/ir.model.access.csv',
        'views/space_mision_menuitems.xml',
    ],
    'demo': [
        'demo/spacemision_demo.xml',
    ],
    'installable':True,
    'auto_install': False,
    'aplication': True,
}
