import os
import webapp2
import jinja2

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)

   class MainPage(webapp2.RequestHandler):
      def get(self):
        welcome_template = jinja_env.get_template("templates/welcome_template.html")
        self.response.write(welcome_template.render())

        app = webapp2.WSGIApplication([
             ('/', MainPage),
        ], debug=True)
