# -*- coding: utf-8 -*-

from odoo import models, fields, api
    
class Project(models.Model):
    #_inherit = {'project.project': ''}
    _inherit = ['project.project']
    
    #New field
    mission_id = fields.Many2one(comodel_name='spacial_mission.mission',
                                string='Related Mission')
