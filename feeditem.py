from django.utils import simplejson as json

class feeditem:
	def __init__(self, title, link, description):
		self.title = title
		self.description = description
		self.link = link

class feeditemjsonencoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, feeditem):
			return {'title': obj.title, 'description': obj.description,'link': obj.link}
		return json.JSONEncoder.default(self, obj)