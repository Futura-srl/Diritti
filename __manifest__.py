{
    'name': 'diritti',
    'version': '19.0.1.0.0',
    'author': "Luca Cocozza",
    'application': True,
    'description': "Aggiunta del campo groups_ids da poter integrare nei moduli.",
    'depends': ['fleet','carburante'],
    'data': [
        # # Settaggi per accesso ai contenuti
        'data/ir.model.access.csv',
        # # Caricamento delle view,
        'view/groups_field.xml',
        'view/groups.xml',
    ],
}
