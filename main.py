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
import webapp2
import caesar
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Caesar</title>
</head>
<body>
    <h1>Web Caesar</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

def buildPage(textarea):
    input_box = ("""
        <form action="/" method="post">
            <div>
                <label>
                    Enter a message:<br>
                    <textarea name="message" style="height: 100px; width: 400px"/>""" + textarea + """</textarea>
                </label>
                <br>
                <label>
                    Rotate by:<br>
                    <input type="number" name="rotate-by" required/>
                </label>
                <br>
                <input type="submit" value="Encrypt"/>
            </div>
        </form>
        """)
    page_content = page_header + input_box + page_footer
    return page_content

    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(buildPage(""))

    def post(self):
        # look inside the request to figure out what the user typed
        message = self.request.get("message")
        rotate = int(self.request.get("rotate-by"))
        encrypted_message = caesar.encrypt(message, rotate)
        output = cgi.escape(encrypted_message)

        # build response content
        self.response.write(buildPage(output))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
