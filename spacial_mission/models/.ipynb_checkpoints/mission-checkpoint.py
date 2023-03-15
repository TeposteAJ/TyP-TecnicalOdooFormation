# -*- coding: utf-8 -*-

import string, random
from odoo import models, fields, api

class Mission(models.Model):
    
    _name = 'spacial_mission.mission'
    _description = 'Mission Info'
    
    
    def _default_mission_id(self):
        rand_letters = random.sample(string.ascii_letters, 3)
        rand_num = random.randint(1000, 9999)
        id = "".join(rand_letters)  
        id = id + str(rand_num)
        return id
    
                        
    mission_id = fields.Char(string='Mission ID',default=_default_mission_id)
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
    

    # === New numerics fields Cost & budgets ===
    budget_fuel = fields.Float(string='Fuel', default=0.00)
    budget_supplies = fields.Float(string='Supplies', default=0.00)
    budget_staff = fields.Float(string='Staff Cost', default=0.00)
    budget_crew = fields.Float(string='Crew Cost', default=0.00)
    
    budget_initial = fields.Float(string='Mission Budget', default=0.00)
    cost = fields.Float(string='Actually Total Cost', default=0.00)
    budget_emergency = fields.Float(string='Emergency Fonds')

    # === Related fields ===
    spaceship_id = fields.Many2one(comodel_name='spacial_mission.spaceship',
                                   string='Spaceship', ondelete='restrict')
    model = fields.Char(related='spaceship_id.model', string='Model')
    captain = fields.Char(related='spaceship_id.captain', string='Captain')
    
    crew_mission = fields.Many2many(comodel_name='res.partner', 
                                    string='Crew Members')
    #Corregir esto no puede llamarse crew_mission es un many2many debe ser algo como crew_ids
    project_ids = fields.One2many(comodel_name='project.project',
                                  inverse_name='mission_id')
    
    
    # === Computed fields ===
   
    days = fields.Char(compute='_compute_days', string='Durations days')
    
    # === COMPUTES ===
   #def _compute_mission_id(self): 
    #    for record in self:
     #       if record.name:
      #          rand_letters = random.sample(string.ascii_letters, 3)
       #         rand_num = random.randint(1000, 9999)
        #        id = "".join(rand_letters)  
         #       id = id + str(rand_num)
          #      record.mission_id = id
                
                
    @api.depends('launch_date', 'return_date')           
    def _compute_days(self):
        for record in self:
            #record.days = '100'
            if record.return_date and record.launch_date is not None:
                record.days = str(record.return_date - record.launch_date)
            else:
                record.days = '0 days'
                #Si no agrego este else, me da error al tratar de grabar la info.
        
