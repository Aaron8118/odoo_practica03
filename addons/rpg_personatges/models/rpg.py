
from odoo import models, fields


class RPGHabilitat(models.Model):
    _name = 'rpg.habilitat'
    _description = 'Habilitats dels personatges'

    name = fields.Char(string='Nom de l’habilitat', required=True)
    descripcio = fields.Text(string='Descripció')


class RPGClasse(models.Model):
    _name = 'rpg.classe'
    _description = 'Classe del personatge'

    name = fields.Char(string='Nom de la classe', required=True)


class RPGPersonatge(models.Model):
    _name = 'rpg.personatge'
    _description = 'Personatge RPG'

    name = fields.Char(string='Nom del personatge', required=True)

    imatge = fields.Binary(
        string='Imatge de l’heroi',
        attachment=True
    )

    data_creacio = fields.Date(
        string='Data de creació'
    )

    habilitat_ids = fields.Many2many(
        'rpg.habilitat',
        string='Habilitats'
    )

    classe_id = fields.Many2one(
        'rpg.classe',
        string='Classe'
    )


class RPGAvaluador(models.Model):
    _name = 'rpg.avaluador'
    _description = 'Avaluador automàtic RPG'

    nom_model = fields.Char(
        string='Nom tècnic del model',
        required=True
    )

    ext_id = fields.Char(
        string='ID extern complet',
        required=True
    )

    requisit = fields.Selection(
        [
            ('img', 'Imatge'),
            ('ref', 'Referència'),
            ('dat', 'Data Calculada'),
            ('m2m', 'Relació Many2many'),
        ],
        string='Requisit',
        required=True
    )
