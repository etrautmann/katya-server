
import os
import cherrypy


# a hack to make cherrypy work on heroku
from cherrypy.process import servers

def fake_wait_for_occupied_port(host, port): return
servers.wait_for_occupied_port = fake_wait_for_occupied_port



class HelloWorld(object):
    def index(self):
        return "Hello World test 2!"
    index.exposed = True




cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})

cherrypy.quickstart(HelloWorld())

