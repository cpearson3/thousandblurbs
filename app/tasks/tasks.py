#  Import supporting libs
from flask import Flask
import logging

import EmailTask

# Flask app app instance
app = Flask(__name__)
app.debug = True

# Define EmailTask Url Routes
app.add_url_rule('/_tasks/email/notification', view_func=EmailTask.Notification, methods=['POST'])