"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

    2016 - Cisco Systems inc.
"""

import flask_sijax
from flask import render_template, g
from app import app
from handlers.netconf_handler import NetConfHandler

"""
Map web URL to templates
"""


@flask_sijax.route(app, '/')
def main():
    # Check if is a sijax request
    if g.sijax.is_sijax_request:

        # Create a new handler
        g.sijax.register_object(NetConfHandler())

        # Process the request
        return g.sijax.process_request()

    # Return index page
    return render_template('main.html')