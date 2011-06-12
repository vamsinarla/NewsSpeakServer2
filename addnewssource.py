from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext.db import djangoforms

import cgi
import newssource

class NewsSourceForm(djangoforms.ModelForm):
	class Meta:
		model = newssource.NewsSource
		exclude = ['preferred']

class AddNewsSourceHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write('<html><body>'
                                '<form method="POST" '
                                'action="/">'
                                '<table>')
		self.response.out.write(NewsSourceForm())
		self.response.out.write('</table>'
                                '<input type="submit">'
                                '</form></body></html>')

	def post(self):
		data = NewsSourceForm(data = self.request.POST)
		
		if data.is_valid():
			# Map the data from djangoform model to db model and save to datastore
			entity = data.save(commit = False)
			entity.preferred = True # Default to preferred sources only for now
			if entity.categories:
				entity.hasCategories = True
			entity.put()
			self.redirect('/')
		else:
			# Reprint the form
			self.response.out.write('<html><body>'
                                '<form method="POST" '
                                'action="/">'
                                '<table>')
        	self.response.out.write(data)
      		self.response.out.write('</table>'
                                    '<input type="submit">'
                                    '</form></body></html>')

def main():
	application = webapp.WSGIApplication([('/addsource', AddNewsSourceHandler)],
										 debug=True)
	
	run_wsgi_app(application)
	
if __name__ == "__main__":
	main()