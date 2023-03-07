# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SpaceshipModel(models.Model):

    _name = 'spacial_mision.spaceship'  #nombre de modulo (carpeta) . nombre del archivo del modelo
    _description = 'Spaceship Info'

    name = fields.Char(string='Title', required=True, index=True)
    active = fields.Boolean(default=True)
    type = fields.Selection(string='Opciones para elegir',
                            selection=[('freighter', 'Freighter'),
                                       ('transport', 'Transport'),
                                       ('scout_ship', 'Scout ship'),
                                       ('fighter','Fighter'),],
                            copy=False,
                            )
    model = fields.Char(string='Model', required=True, index=True)
    build_date = fields.Date(string='Build date')
    chaptain = fields.Char(string='Chaptain', required=True, index=True)
    required_crew = fields.Integer(default=0, required=True, string='Required Crew')
    length = fields.Float(default=0, string='Spaceship Length [meters]')
    width = fields.Float(default=0, string='Spaceship Width [meters]')
    engine_number = fields.Char(string='Engine Number')
    fuel_type = fields.Selection(string='Fuel Type',
                                 selection=[('solid_fuel','Solid Fuel'),
                                           ('liquid_fuel','Liquid Fuel'),],
                                )
    max_ocupation = fields.Integer(default=2, string='Max Number of Tripulants')