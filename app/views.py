"""
Main point of entry for the web application

"""

import flask_sijax
from flask import render_template, g, send_from_directory
from app import app
from handlers.netconf_handler import NetConfHandler

@flask_sijax.route(app, '/')
def service_template():
    # Check if is a sijax request
    if g.sijax.is_sijax_request:

        # Create a new handler
        g.sijax.register_object(NetConfHandler())

        # Process the request
        return g.sijax.process_request()

    # Return index page
    return render_template('main.html')