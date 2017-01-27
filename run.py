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

from app import app

"""
To make the application visible outside the local server, change the loopback ip address for your given ip.
You can also change the port that the application will be listening.
To change the default https protocol for http, remove the ssl_context parameter from the last line
"""
__author__ = 'Santiago Flores Kanter (sfloresk@cisco.com)'

# IP and PORT constants. The following values will be use to start the web server
IP = '0.0.0.0'
PORT = 5008

# Create a context with https key and certificates located in the local project directory
context = ('NCBCert.pem', 'NCBKey.pem')

# Run the web server according to the given IP, port and https context
app.run(host=IP, debug=True, port=PORT, ssl_context=context, threaded=True)

