# -*- coding: utf-8 -*-

{
    'name': 'Space Mission',
    'version': '1.0',
    'summary': """ Spacial Mision App to manage the mision to the space""",
    # 'description': """
    #     Library App to manage books and clients, that need help to rent books.
    #     - Clients
    #     - Books
    # """,
    'author': 'Ángela Teposte',
    'website': 'https://github.com/TeposteAJ',
    'license': 'GPL-3',
    'category': 'Custom Modules/ Tech Training',
    'depends': ['base'],
    'data': [
        'security/spacial_mission_groups.xml',
        'security/spacial_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menuitems.xml',
        'views/spaceship_views.xml',
        'views/mission_views.xml',
    ],
    'demo': [
        'demo/spaceship_demo.xml',
        'demo/mission_demo.xml',
    ],
    'installable':True,
    'auto_install': False,
    'aplication': True,
}
