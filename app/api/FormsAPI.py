#  Import supporting libs

from google.appengine.api import taskqueue
from flask import Flask, render_template, url_for, request, Response, jsonify
from wtforms import Form, StringField, TextAreaField, validators

import json
import logging

# import project modules
from .. import config
from .. import services
from .. import models

# Get Submissions
def getSubmission():

	# TODO: Better logging
	logging.warning('FormsAPI Call: getSubmission')

	# get objects
	data = services.FormService.GetAll()

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

# Export Submissions
def exportSubmissions():

	logging.warning('FormsAPI Call: exportSubmissions')
	
	# get objects
	data = services.FormService.GetAll()

	# Add header to CSV output
	csv_output = 'Data, Namespace ID, Form ID, Datetime, Client IP Address\n'

	# Convert data to comma separated list
	for i in data:
		csv_output += ','.join([i['data'], i['namespaceID'], i['formID'], i['datetime'],i['clientIP']]) + '\n'

	try:
		return Response(csv_output, mimetype="text/csv")

	except Exception as e:
		# TODO: return proper error response
		return str(e)

# Submission Form 
# - Form ID is required
class SubmissionForm(Form):
	formID = StringField('formID', [validators.Required(), validators.length(max=50)])
	namespaceID = StringField('namespaceID', [validators.Required(), validators.length(max=50)])
	apiKey = StringField('apiKey')

def saveSubmission():
	
	data = {}
	form = SubmissionForm(request.form)

	logging.warning('FormsAPI Call: saveSubmission')
	logging.warning('Referrer: ' + request.remote_addr)

	# validate form submission
	if form.validate():
		# FORM DATA IS VALID
		
		# 0.2.0 - check API key
		# 0.3.0 - API key defined in config module

		data = {
			'data': {},
			'formID': request.form.get('formID'),
			'namespaceID': request.form.get('namespaceID'),
			'key': request.form.get('key'),
			'clientIP': request.remote_addr
		}
		
		for i in request.form.keys():
			data['data'][i] = request.form.get(i)

		logging.warning('key passed: ' + str(data['key']))

		# update submission
		try:
			services.FormService.Save(data)
		except Exception as e:
			# Oh no, something went wrong
			# return response object with error status code
			
			logging.warning('Exception occured: ' + str(e))
			
			resp = jsonify({
				'status': 400,
				'error': str(e)
			})

			resp.status_code = 400
			return resp	
		
		# success, trigger email notification
		
		if config.SEND_NOTIFICATIONS:
			logging.warning('Trigger Email Notification Task')
			services.EmailService.sendNotification(data):
		
		# success
		resp = jsonify({
			'status': 200,
			'message': 'Successful save'
		})

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
def deleteSubmission():
	
	logging.warning('FormsAPI Call: deleteSubmission')

	# get key
	try:
		key = request.form['key']

		if key:

			if services.FormService.Delete(key):

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
			'error': 'Error in deleteSubmission controller: ' + str(e)
		})

		return resp

# save list of submissions
def saveSubmissions():
	
	logging.warning('FormsAPI Call: saveSubmissions')

	# GET and CONVERT data
	try:

		# get post data
		post_data = request.form['data']

		# convert json
		v_data = json.loads(post_data)

	except Exception as e:
		resp = jsonify({
			'status': 400,
			'error': 'Error retrieving POST data: ' + str(e)
		})

		return resp

	# Loop and save submissions
	try:
		for i in v_data:

			#return Response(json.dumps(i), mimetype="text/json")

			new_key = services.FormService.Save(i)

			if new_key:
				logging.warning('saved new key: ' +  str(new_key))
			else:
				logging.warning('could not save submission info: ' + str(i))

	except Exception as e:
		resp = jsonify({
			'status': 400,
			'error': 'Error parsing POST data: ' + str(e)
		})

		return resp
		

	resp = jsonify({
		'status': 200,
		'message': 'Saved list of submissions'
	})

	return resp