
{
    'name': 'Matricula Estudis',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestió de matrícules en cursos',
    'depends': ['base'],
    'data': [
        'views/curs_views.xml',
        'views/alumne_views.xml',
        'views/inscripcio_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}


