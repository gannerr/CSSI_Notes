# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Hello, Sloth.</h1>')

class SlothsPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Andy Loves Sloths!</h1>')

class PandasPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        # self.response.write('<h1>Andrew Loves Pandas!</h1>')
        template = JINJA_ENVIRONMENT.get_template('templates/pandas.html')
        self.response.write(template.render())

class AnimalsPage(webapp2.RequestHandler):
    def get(self):
        animal_input = "default"
        if(self.request.get('animal')):
            animal_input = self.request.get('animal')
        name_input = self.request.get('name')
        values = {
            "name": animal_input,
            "animal": name_input
        }
        adjective = self.request.get('adj')
        self.response.headers['Content-Type'] = 'text/html'
        #self.response.write('<h1>' + name_input + ' Loves ' + adjective + ' ' + animal_input + '!</h1>')
        template = JINJA_ENVIRONMENT.get_template('templates/animals.html')
        self.response.write(template.render(values))



# The app config
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sloths', SlothsPage),
    ('/pandas', PandasPage),
    ('/animals', AnimalsPage)
], debug=True)
