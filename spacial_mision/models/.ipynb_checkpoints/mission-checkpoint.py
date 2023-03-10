# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    
    _name = 'spacial_mision.mission'
    _description = 'Mission Info'
    
    name = fields.Char(string='Title', required=True, index=True)
    mission_id = pass #compute
    type = fields.Selection(string='Category',
                            selection=[('exploration', 'Exploration'),
                                       ('for_supplies', 'For Supplies'),
                                       ('urgent','Urgent'),],
                            )
    launch_date = pass
    return_date = pass
    days = pass #compute
    spaceship = pass #one2many
    crew_mission = pass #many2many
    lau
    