#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
from django.utils import simplejson as json
import logging, cgi, datetime
import feeditem
import feedparser


class FeedHandler(webapp.RequestHandler):
    def get(self):
        feed_url = self.request.get('url')

        logging.info("Feedurl in get = " + feed_url)
        
        try:
            feedInput = urlfetch.fetch(feed_url)
        except:
            raise Exception("Cannot retrieve feedInput url")
        
        parsed_feed = feedparser.parse(feedInput.content)
        if parsed_feed.bozo == 1:
            raise Exception("Cannot parse given url")
        
        feed_items = []
        
        for entry in parsed_feed.entries[:5]:
            item = feeditem.feeditem(entry.title,
                                        entry.link,
                                        entry.summary)
            item_json = feeditem.feeditemjsonencoder().default(item)
            feed_items.append(item_json)
            logging.info(item_json)
            
        self.response.out.write(feed_items)

def main():
    application = webapp.WSGIApplication([('/feed', FeedHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
