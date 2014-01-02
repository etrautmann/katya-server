
import os
import cherrypy


# a hack to make cherrypy work on heroku
from cherrypy.process import servers

def fake_wait_for_occupied_port(host, port): return
servers.wait_for_occupied_port = fake_wait_for_occupied_port



# class HelloWorld(object):
#     def index(self):
#         return "Hello World test 2!"
#     index.exposed = True


class Page:
    def contents(self):
        return '''
            Temperature setpoint: %s

            <p></p>
            <p></p>
            <p></p>
            
            <form action="setTemp" method="GET">
            Enter Temperature Setpoint
            <input type="text" name="name" />
            <input type="submit" />
            </form>

            Current Temperature: %s 


            ''' % (self.tempSetPoint, self.currentTemp)

class WelcomePage(Page):

    def __init__(self):
        # Ask for the user's name.
        self.tempSetPoint = 104
        self.currentTemp = 100

    def index(self):
        return self.contents()
        
        
    index.exposed = True

    def setTemp(self, name = None):
        # CherryPy passes all GET and POST variables as method parameters.
        # It doesn't make a difference where the variables come from, how
        # large their contents are, and so on.
        #
        # You can define default parameter values as usual. In this
        # example, the "name" parameter defaults to None so we can check
        # if a name was actually specified.

        if name:
            # Greet the user!
            self.tempSetPoint = name
            # return "Temperature Setpoint: %s " % self.tempSetPoint
            return self.contents()
            #return self.index

        else:
            if name is None:
                # No name was specified
                return 'Enter Temperature Setpoint <a href="./">here</a>.'
            else:
                return 'No, really, enter temp setpoint <a href="./">here</a>.'
    setTemp.exposed = True


root = WelcomePage()



cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})

# cherrypy.quickstart(HelloWorld())
cherrypy.quickstart(WelcomePage())

