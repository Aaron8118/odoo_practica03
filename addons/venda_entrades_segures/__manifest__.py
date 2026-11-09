{
    'name': 'Venda Entrades Segures',
    'version': '1.0',
    'category': 'Events',
    'summary': 'Gestió d entrades nominals',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/etiquetes.xml',
        'views/esdeveniment_views.xml',
        'views/tiquet_views.xml',
        'views/etiqueta_views.xml',
    ],
    'installable': True,
    'application': True,
}
