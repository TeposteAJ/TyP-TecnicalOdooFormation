# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SpaceshipModel(models.Model):

    _name = 'spacial_mision.spaceship'  #nombre de modulo (carpeta) . nombre del archivo del modelo
    _description = 'Spaceship Info'

    name = fields.Char(string='Title', required=True, index=True)
    active = fields.Boolean(default=True)
    type = fields.Selection(string='Spaceship Type',
                            selection=[('freighter', 'Freighter'),
                                       ('transport', 'Transport'),
                                       ('scout_ship', 'Scout ship'),
                                       ('fighter','Fighter'),],
                            copy=False,
                            )
    model = fields.Char(string='Model', required=True, index=True)
    build_date = fields.Date(string='Build date')
    chaptain = fields.Char(string='Captain', required=True, index=True)
    required_crew = fields.Integer(default=0, required=True, string='Required Crew')
    length = fields.Float(default=0, string='Spaceship Length [meters]')
    width = fields.Float(default=0, string='Spaceship Width [meters]')
    engine_number = fields.Char(string='Engine Number')
    fuel_type = fields.Selection(string='Fuel Type',
                                 selection=[('solid_fuel','Solid Fuel'),
                                           ('liquid_fuel','Liquid Fuel'),],
                                )
    max_ocupation = fields.Integer(default=2, string='Max Crew')
    
    @api.constrains('length','width')
    def _check_size(self):
        for record in self:
            if record.width > record.length:
                raise UserError('"Spaceship Width" cannot be larger that "Spaceship Length".')
                
    
    @api.onchange('model')
    def _check_integer(self):
        for record in self:
            if record.model and len(record.model) <= 2:
                raise ValidationError(' "Model" must be larger that 2 character.')
                
    #@api.depends()
    #