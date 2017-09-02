#  Import supporting libs
from flask import Flask, render_template, url_for, request, Response, jsonify, abort
from wtforms import Form, StringField, TextAreaField, validators

import json
import logging

# import project modules
from .. import config
from .. import services
from .. import models

import FormsAPI
import NamespaceAPI

# Flask app app instance
app = Flask(__name__)
app.debug = True

# check API key
@app.before_request
def check_api_key():
	logging.warning('testing api key')
	if config.API_KEY:
		
		# get key from url param (get) or form data (post)
		if request.method == 'GET':
			key = request.args.get('apiKey')
		else:
			# POST PUT and DELETE
			key = request.form.get('apiKey')
		
		# log the key values
		logging.warning('key passed: %s, config: %s' % (key, config.API_KEY))
		
		if key != config.API_KEY:
			# return response object with error status code
			abort(401)
		else:
			pass

# limit access to allowed domains
@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', config.ALLOWED_DOMAINS)
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', '*')
	return response

# Define FormsAPI Url Routes
app.add_url_rule('/_api/forms/',  view_func=FormsAPI.getSubmission)
app.add_url_rule('/_api/forms/save',  view_func=FormsAPI.saveSubmission, methods=['POST'])
app.add_url_rule('/_api/forms/saveList',  view_func=FormsAPI.saveSubmissions, methods=['POST'])
app.add_url_rule('/_api/forms/delete',  view_func=FormsAPI.deleteSubmission, methods=['POST'])
app.add_url_rule('/_api/forms/export.csv',  view_func=FormsAPI.exportSubmissions)

# Define NamespaceAPI Url Routes
app.add_url_rule('/_api/namespace/', view_func=NamespaceAPI.getNamespaces)
app.add_url_rule('/_api/namespace/save', view_func=NamespaceAPI.saveNamespace, methods=['POST'])
app.add_url_rule('/_api/namespace/delete',  view_func=NamespaceAPI.deleteNamespace, methods=['POST'])
