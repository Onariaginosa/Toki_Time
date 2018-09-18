import os
import webapp2
import jinja2

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)

class StartPage(webapp2.RequestHandler):
      def get(self):
        start_template = jinja_env.get_template("templates/welcome.html")
        self.response.write(start_template.render())

class SettingsPage(webapp2.RequestHandler):
    def get(self):
        settings_template = jinja_env.get_template("templates/settings.html")
        self.response.write(settings_template.render())

class MainPage(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template("templates/main.html")
        self.response.write(main_template.render())


app = webapp2.WSGIApplication([
    ('/', StartPage),('/settings', SettingsPage),('/main', MainPage),], debug=True)
