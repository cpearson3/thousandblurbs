#  Import supporting libs
from flask import Flask, render_template, url_for, request, Response, jsonify, abort
from wtforms import Form, StringField, TextAreaField, validators

import json
import logging

# import project modules
from .. import config
from .. import services
from .. import models

import CampaignAPI
import BlurbsAPI
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

# Define CampaignAPI Url Routes
app.add_url_rule('/_api/campaign/', view_func=CampaignAPI.getCampaigns)
app.add_url_rule('/_api/campaign/save', view_func=CampaignAPI.saveCampaign, methods=['POST'])
app.add_url_rule('/_api/campaign/delete',  view_func=CampaignAPI.deleteCampaign, methods=['POST'])

# Define BlurbsAPI Url Routes
app.add_url_rule('/_api/blurbs/', view_func=BlurbsAPI.getBlurbs)
app.add_url_rule('/_api/blurbs/get', view_func=BlurbsAPI.getBlurb)
app.add_url_rule('/_api/blurbs/save', view_func=BlurbsAPI.saveBlurb, methods=['POST'])
app.add_url_rule('/_api/blurbs/delete',  view_func=BlurbsAPI.deleteBlurb, methods=['POST'])
