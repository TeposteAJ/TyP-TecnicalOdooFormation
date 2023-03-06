# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):

    _name = 'volunteers.task'
    _description = 'Task Info'

name = fields.Char(string='Title', required=True, index=True)
start_time = fields.Datetime(string='Start date')
stop_time = fields.Datetime(string='Ending')
ocurrences = fields.Integer(default=0)
description = fields.Text(string='Task description')
task_type = fields.Selection(string='Opciones para elegir',
                             selection=[('opcion1', 'OPCION 1'),
                                        ('opcion2', 'OPCION 2'),
                                        ('opcion3', 'OPCION 3'),],
                             copy=False,
                            )
active = fields.Boolean(default=True)