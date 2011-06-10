from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
from django.utils import simplejson as json
import logging
import cgi
import datetime

class ArticleHandler(webapp.RequestHandler):
	alchemy_url = 'http://alchemy.com'
	
    def post(self):
    	article_url = self.request.get('url')
    	
    	
def main():
    application = webapp.WSGIApplication([('/article', ArticleHandler),
    									 ('/article_meta', ArticleMetaDataHandler)], 
                                         debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()