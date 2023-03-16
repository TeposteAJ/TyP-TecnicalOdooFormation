# -*- coding: utf-8 -*-

from xmlrpc import client

url = 'https://teposteaj-typ-tecnicalodooformation-spacial-mission-7615970.dev.odoo.com'
db = 'teposteaj-typ-tecnicalodooformation-spacial-mission-7615970'
username = 'admin'
password = 'osito'

# key api , para probar la contraseña de osito
# 9ab3882a3f6f68c5ca7da42acaeb0bfbfe2e7906

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
#print(common.version())

uid = common.authenticate(db, username, password, {})
#print(uid)


models = client.ServerProxy("{}/xmlrpc/2/object".format(url))
#print(models)

#Verificando accesos del modelo spaceship:
model_access = models.execute_kw(db, uid, password,
                                 'spacial_mission.spaceship', 'check_access_rights',
                                 ['read'], {'raise_exception': False})
print(model_access)

new_spaceship = models.execute_kw(db, uid, password,
                                 'spacial_mission.spaceship', 'create',
                                 [
                                     {
                                         'name': "ScriptNave",
                                         'type': "scout_ship",
                                         'active': True,
                                         'model': "SCRIPT546",
                                         'captain': "Buzz LightYear",
                                          'required_crew': 8,
                                     }
                                 ]
                                    )
print(new_spaceship)



