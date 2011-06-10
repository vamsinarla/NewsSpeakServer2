from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
from django.utils import simplejson as json
import logging
import cgi
import datetime
import feeditem
import feedparser


class FeedHandler(webapp.RequestHandler):
    def post(self):
        feed_url = self.request.get('url')

        try:
            feed_input = urlfetch.fetch(feed_url)
        except:
            raise Exception("Cannot retrieve feedInput url")
        
        parsed_feed = feedparser.parse(feed_input.content)
        if parsed_feed.bozo == 1:
            raise Exception("Cannot parse given url")
        
        feed_items = []
        
        for entry in parsed_feed.entries:
            item = feeditem.feeditem(entry.title,
                                     entry.link,
                                     entry.summary)
            item_json = feeditem.feeditemjsonencoder().default(item)
            feed_items.append(item_json)

        feed_info = parsed_feed.feed
        self.response.out.write(json.dumps({
                                            "title": feed_info.title,
                                            "language": feed_info.language,
                                            "subtitle":feed_info.subtitle,
                                            "entries": feed_items }))
        
def main():
    application = webapp.WSGIApplication([('/feed', FeedHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
