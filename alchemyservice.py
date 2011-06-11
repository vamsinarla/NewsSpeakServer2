from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
from django.utils import simplejson as json
import urllib
import logging
import cgi
import datetime

class alchemyservice:
	alchemy_base_url = 'http://access.alchemyapi.com/calls/url/'
	alchemy_api_key = '3dd078fdf99f03a052aaa48579a3db2a4e9520a9'
	
	# Support APIs
	get_content = 'URLGetText'
	get_entities = 'URLGetRankedNamedEntities'
	
	def getContent(self, url, format):
		
		# Construct the api call
		api_url = self.alchemy_base_url + self.get_content
		
		api_args = urllib.urlencode({ "url": url,
			  					   "apikey": self.alchemy_api_key,
					 			   "outputMode": format })

		article_content = None			
		try:
			article_content = urlfetch.fetch(url = api_url,
											 payload = api_args,
											 method = urlfetch.POST)
		except:
			logging.error("Error at fetching url = " + url)
		
		return article_content.content
	
	def getEntityData(self, url, format):
		
		# Construct the api call
		api_url = self.alchemy_base_url + self.get_entities
		
		api_args = urllib.urlencode({ "url": url,
					 			   "apikey": self.alchemy_api_key,
					 			   "outputMode": format })
		
		article_entities = None
		try:
			article_entities = urlfetch.fetch(url = api_url,
											  payload = api_args,
											  method = urlfetch.POST)
		except:
			logging.error("Unable to fetch entities for url = " + url)
			
		return article_entities.content
