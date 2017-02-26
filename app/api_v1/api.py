# Thousandblurbs API v0.2.0

# It is highly recommended that you set an API key per project
THOUSANDBLURBS_API_KEY = "123456789"

YOURNAME = ""
SENDGRID_API_KEY = ""
SENDGRID_SENDER = ""

#  Import supporting libs
from flask import Flask, render_template, url_for, request, Response, jsonify
from wtforms import Form, StringField, TextAreaField, validators

import json

import logging

# import services and models
from .. import services
from .. import models

# Flask app app instance
app = Flask(__name__)
app.debug = True

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', '*')
	return response

# Get Submissions
@app.route('/_api/v1/submissions/')
def getSubmissions():

	# TODO: Better logging
	logging.warning('API Call: getSubmissions')

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
@app.route('/_api/v1/submissions/export')
def exportSubmissions():

	logging.warning('API Call: exportSubmissions')
	
	# get objects
	data = services.FormService.GetAll()

	# Add header to CSV output
	csv_output = 'Data, Datetime\n'

	# Convert data to comma separated list
	for i in data:
		csv_output += ','.join([i['data'], i['formID'], i['datetime']]) + '\n'

	try:
		return Response(csv_output, mimetype="text/csv")

	except Exception as e:
		# TODO: return proper error response
		return str(e)

# Submission Form 
# - Form ID is required
class SubmissionForm(Form):
	formID = StringField('formID')
	apiKey = StringField('apiKey')

@app.route('/_api/v1/save/', methods = ['POST'])
def saveSubmission():
	
	data = {}
	form = SubmissionForm(request.form)

	logging.warning('API Call: saveSubmission')
	
	

	# validate form submission
	if form.validate():
		# FORM DATA IS VALID
		
		# 0.2.0
		# check API key
		if THOUSANDBLURBS_API_KEY:
			logging.warning('testing api key')
			key = request.form.get('apiKey')
			
			if key != THOUSANDBLURBS_API_KEY:

				# return response object with error status code
				resp = jsonify({
					'status': 400,
					'error': 'API key did not validate'
				})
		
				resp.status_code = 400
				return resp
			else:
				pass

		data = {
			'data': {},
			'formID': request.form.get('formID'),
			'key': request.form.get('key')
		}
		
		for i in request.form.keys():
			data['data'][i] = request.form.get(i)

		logging.warning('key passed: ' + str(data['key']))

		# update submission
		try:
			if services.FormService.Save(data):
				
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
					'error': 'Could not save contact'
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
@app.route('/_api/v1/delete/', methods = ['POST'])
def deleteSubmission():
	
	logging.warning('API Call: deleteSubmission')

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
@app.route('/_api/v1/save/list', methods = ['POST'])
def saveList():
	
	logging.warning('API Call: saveList')

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