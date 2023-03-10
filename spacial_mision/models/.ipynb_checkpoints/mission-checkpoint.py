# -*- coding: utf-8 -*-

import string, random
from odoo import models, fields, api

class Mission(models.Model):
    
    _name = 'spacial_mision.mission'
    _description = 'Mission Info'
    
    name = fields.Char(string='Title', required=True, index=True)
    active = fields.Boolean(default=True)
    type = fields.Selection(string='Category',
                            selection=[('exploration', 'Exploration'),
                                       ('for_supplies', 'For Supplies'),
                                       ('urgent','Urgent'),],
                            )
    goal = fields.Text(string='Description')
    launch_date = fields.Date(string='Launch date')
    return_date = fields.Date(string='Return date')

    # === Related fields ===
    spaceship_id = fields.Many2one(comodel_name='spacial_mision.spaceship',
                                   string='Spaceship', ondelete='restrict')
    model = fields.Char(related='spaceship_id.model', string='Model')
    captain = fields.Char(related='spaceship_id.chaptain', string='Captain')
    
    crew_mission = fields.Many2many(comodel_name='res.partner', 
                                    string='Crew Members')
    
    # === Computed fields ===
    mission_id = fields.Char(compute='_compute_mission_id', string='Mission ID')
    days = fields.Char(compute='_compute_days', string='Durations days')
    
    # === COMPUTES ===
    def _compute_mission_id(self): 
        for record in self:
            if record.spaceship_id:
                rand_letters = random.sample(string.ascii_letters, 3)
                rand_num = random.randint(1000, 9999)
                id = "".join(rand_letters)  
                id = id + str(rand_num)
                record.mission_id = id
                
    @api.depends('launch_date', 'return_date')           
    def _compute_days(self):
        for record in self:
            record.days = record.return_date - record.launch_date
        
