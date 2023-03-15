# -*- coding: utf-8 -*-

from odoo import models,fields, api


class ProjectWizard(models.TransientModel):
    _name = 'spacial_mission.project.wizard'
    _description = 'Wizard: Quick Project for Mission'
    
    
    def _default_mission(self):
        return self.env['spacial_mission.mission'].browse(self._context.get('active_id','NO ENCONTRADO'))
    
    mission_id = fields.Many2one(comodel_name='spacial_mission.mission',
                                  string='Mission',
                                  required=True,
                                  default=_default_mission)
    #opción: mission_id = field.Many2one(comodel_name='spacial_mission.project', string='Mission', required=True,
                                         #default=lambda self: self.env.context.get('active_id'))
    name = fields.Many2one(comodel_name='project.project', string='Project Name', default="Project No name")
    description = fields.Many2one(comodel_name='project.project', string='Project Description')
    active = fields.Many2one(comodel_name='project.project', string='active')
    label_tasks = fields.Many2one(comodel_name='project.project')
    user_id = fields.Many2one(comodel_name='project.project')
    date_start = fields.Many2one(comodel_name='project.project')
    is_favorite = fields.Many2one(comodel_name='project.project')
    privacy_visibility = fields.Many2one(comodel_name='project.project')
        
    # Project Sharing fields
    collaborator_ids = fields.Many2many(comodel_name='project.project')
    collaborator_count = fields.Many2one(comodel_name='project.project')
    
    
    def create_project(self):
        project_id = self.env['project.project'].create({
            'mission_id': self.mission_id.id,
            'name': self.name,
            'description': self.description,
            'active': self.active,
            'label_task': self.label_task,
            'user_id': self.user_id.id,
            'date_start': self.date_start,
            'is_favorite': self.is_favorite,
            'privacy_visibility': self.privacy_visibility,
            'collaborator_ids': self.collaborator_ids,
            'collaborator_count': self.collaborator_count,
        })
        #mission_active = self.env['spacial_mission.mission'].search([("active", "=", True)], limit = 1)
        #is mission_active:
         #   project_id = self.env['project.project'].create({
          #                'user_id': self.user_id,
           #               'mission_id': self.mission.id,
            #})
    
   

    