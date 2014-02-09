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
import cgi
import datetime
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import urlfetch



def reboot_router():
  url='http://yours.eicp.net:81/userRpm/SysRebootRpm.htm?Reboot=%D6%D8%C6%F4%C2%B7%D3%C9%C6%F7'
  header_authorized='Basic dXNlcjpwYXNzd29yZA=='
  result = urlfetch.fetch(url=url,
                          method=urlfetch.GET,
                          headers={'Authorization': header_authorized })

class MainPage(webapp2.RequestHandler):
  def get(self):
    #self.response.out.write('<html>asdasd</html>')
     
    reboot_router()

app = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
