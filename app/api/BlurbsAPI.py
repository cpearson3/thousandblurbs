
#  Import supporting libs

from google.appengine.api import taskqueue
from flask import Flask, render_template, url_for, request, Response, jsonify
from wtforms import Form, StringField, TextAreaField, validators

from google.appengine.ext import deferred

import json
import logging

# import project modules
from .. import config
from .. import services
from .. import models

# Get Blurbs
def getBlurbs():

	# TODO: Better logging
	logging.warning('BlurbsAPI Call: getBlurb')

	# get objects
	data = services.BlurbService.GetAll()

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

# Blurb Submission Form
# - Blurb ID is required
class BlurbSubmission(Form):
	blurbID = StringField('blurbID', [validators.Required(), validators.length(max=50)])
	namespaceID = StringField('namespaceID', [validators.Required(), validators.length(max=50)])

def saveBlurb():
	
	data = {}
	form = BlurbSubmission(request.form)

	logging.warning('BlurbsAPI Call: saveBlurb')
	logging.warning('Referrer: ' + request.remote_addr)

	# validate blurb submission
	if form.validate():
		data = {
			'blurbID': request.form.get('blurbID'),
			'namespaceID': request.form.get('namespaceID'),
			'content': request.form.get('content'),
			'key': request.form.get('key'),
		}		

		logging.warning('key passed: ' + str(data['key']))

		# update submission
		try:
			result = services.BlurbService.Save(data)

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
		
		if result:
			
			# success
			resp = jsonify({
				'status': 200,
				'message': 'Successful save'
			})

			return resp

		else:
			# fail
			# return response object with error status code
			resp = jsonify({
				'status': 400,
				'error': 'Could not save submission'
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
def deleteBlurb():
	
	logging.warning('BlurbsAPI Call: deleteBlurb')

	# get key
	try:
		key = request.form['key']

		if key:

			if services.BlurbService.Delete(key):

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
			'error': 'Error in deleteBlurb controller: ' + str(e)
		})

		return resp

# save list of submissions
def saveBlurbs():
	
	logging.warning('BlurbsAPI Call: saveBlurbs')

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

			new_key = services.BlurbService.Save(i)

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