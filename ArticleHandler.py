from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
from django.utils import simplejson as json
import logging
import cgi
import datetime
import alchemyservice

class ArticleHandler(webapp.RequestHandler):
	
    def post(self):
    	article_url = self.request.get('url')
    	format = self.request.get('format')
    	
    	article_content = alchemyservice.alchemyservice().getContent(article_url,
    												  				 format)
    	
    	self.response.out.write(article_content)

class ArticleMetadataHandler(webapp.RequestHandler):
	
	def post(self):
		article_url = self.request.get('url')
		format = self.request.get('format')
		
		article_entities = alchemyservice.alchemyservice().getEntityData(article_url,
														  				 format)
		self.response.out.write(article_entities)
		
def main():
    application = webapp.WSGIApplication([('/article/content', ArticleHandler),
    									 ('/article/meta', ArticleMetadataHandler)], 
                                         debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()