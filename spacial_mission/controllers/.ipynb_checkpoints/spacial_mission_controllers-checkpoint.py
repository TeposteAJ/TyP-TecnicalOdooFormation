# -*- coding: utf-8 -*-

from odoo import http


class Mission(http.Controller):
    @http.route('/spacial-mission/', auth='public', website=True)
    def index(self, **kw):
        return "Hello!, world!"
    
    @http.route('/spacial-mission/missions/', auth='public', website=True)
    def missions(self, **kw):
        missions = http.request.env['spacial_mission.mission'.search([])]
        return http.request.render('spacial_mission.mission_website',{
                                        'missions': missions,
                                    })
    
    @http.route('/spacial-mission/<model("spacial_mission.project"):project>/', auth='public', website=True)
    def project(self, project):
        return http.request.render('spacial_mission.project_website', {
            'project': project,
        })
    