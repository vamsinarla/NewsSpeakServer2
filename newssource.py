import cgi
from google.appengine.ext import db

class NewsSource(db.Model):
	title = db.StringProperty()
	type = db.StringProperty(default='newspaper', choices = [
							 'newspaper', 'blog'])
	preferred = db.BooleanProperty(default=False)
	language = db.StringProperty()
	hasCategories = db.BooleanProperty(default=False)
	country = db.StringProperty()
	categories = db.StringListProperty(default=None)
	categoryUrls = db.StringListProperty(default=None)
