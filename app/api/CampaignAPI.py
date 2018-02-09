# CampaignAPI.py

#  Import supporting libs
from flask import Flask, render_template, url_for, request, Response, jsonify
from wtforms import Form, StringField, TextAreaField, validators

import json
import logging

# import project modules
from .. import config
from .. import services
from .. import models

# Get Campaigns
def getCampaigns():

	# TODO: Better logging
	logging.warning('CampaignsAPI Call: getCampaign')

	# get objects
	data = services.CampaignService.GetAll()

	output = []

	# convert datetime to string
	for i in data:
		out = i
		out['datetime'] = str(i['datetime'])
		output.append(out)

	try:
		return Response(json.dumps(output), mimetype="text/json")

	except Exception as e:
		# TODO: return proper error response
		return str(e)

# Campaign Form 
# - Form ID is required
class CampaignForm(Form):
	campaignID = StringField('campaignID')
	description = TextAreaField('description')
	apiKey = StringField('apiKey')

def saveCampaign():
	
	data = {}
	form = CampaignForm(request.form)

	logging.warning('CampaignsAPI Call: saveCampaign')

	# validate form Campaign
	if form.validate():

		data = {
			'data': {},
			'campaignID': request.form.get('campaignID'),
			'description': request.form.get('description'),
			'key': request.form.get('key')
		}

		# update Campaign
		try:
			if services.CampaignService.Save(data):
				
				# success
				resp = jsonify({
					'status': 200,
					'message': 'Successful save'
				})

				return resp
			else:
				# error save data
				resp = jsonify({
					'status': 400,
					'error': 'Could not save'
				})

				resp.status_code = 400
				return resp	

		except Exception as e:
			# Oh no, something went wrong
			# return response object with error status code
			resp = jsonify({
				'status': 400,
				'error': str(e)
			})

			resp.status_code = 400
			return resp	
	
	else:
		# FORM DATA IS INVALID

		# return response object with error status code
		resp = jsonify({
			'status': 400,
			'error': 'form did not validate'
		})

		resp.status_code = 400
		return resp

# delete
def deleteCampaign():
	
	logging.warning('CampaignsAPI Call: deleteCampaign')

	# get key
	try:
		key = request.form['key']

		if key:

			if services.CampaignService.Delete(key):

				resp = jsonify({
					'status': 200,
					'message': 'key passed: ' + key
				})

				return resp
			else:
				resp = jsonify({
					'status': 400,
					'error': 'Could not delete item with key: ' + str(key)
				})

				return resp

		else:

			resp = jsonify({
				'status': 400,
				'error': 'No key passed'
			})

			return resp
	except Exception as e:
		
		resp = jsonify({
			'status': 400,
			'error': 'Error in deleteCampaign controller: ' + str(e)
		})

		return resp
		
def f():
	if config.API_KEY:
		logging.warning('testing api key')
		key = request.form.get('apiKey')
		
		if key != config.API_KEY:

			# return response object with error status code
			resp = jsonify({
				'status': 400,
				'error': 'API key did not validate'
			})
	
			resp.status_code = 400
			return resp
		else:
			pass
