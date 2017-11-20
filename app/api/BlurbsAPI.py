
#  Import supporting libs

from google.appengine.api import taskqueue
from flask import Flask, render_template, url_for, request, Response, jsonify
from wtforms import Form, StringField, TextAreaField, validators

from google.appengine.ext import deferred

import json
import logging
import markdown

# import project modules
from .. import config
from .. import services
from .. import models


# Get single blurb
def getBlurb():
	
	logging.warning('BlurbsAPI call: getBlurb')
	
	try:
		blurbKey = request.args.get('key')
		
		blurb = services.BlurbService.Get(blurbKey)
		
		if blurb:
			data = models.Model.toDict(blurb)
			# convert markdown
			data['content'] = markdown.markdown(data['content'][1:-1].replace('\\n','\n'))
		else:
			data = {
				'content': 'This Blurb Does Not Exist',
				'blurbID': 'No Blurb Here'
			}
		
	except Exception as e:
		resp = jsonify({
			'status': 400,
			'error': 'Error in getBlurb controller: ' + str(e)
		})

		return resp
	
	dataType = request.args.get('dataType')
	
	if dataType == 'json':
		return Response(json.dumps(data), mimetype="text/json")
	else:
		return render_template('blurb.html', data=data)
		
# Get by ID
def getBlurbByID(pID=None):
	
	logging.warning('BlurbsAPI call: getBlurbByID')
	
	if pID:
		blurbID = pID
	else:
		blurbID = request.args.get('id')
	
	if blurbID is None:
		logging.warning('No blurb ID passed.')
		
		resp = jsonify({
			'status': 400,
			'error': 'Parameter Error: Blurb ID'
		})

		return resp
	else:
		logging.warning('blurb id passed: ' + blurbID)
		
	try:
		blurb = services.BlurbService.GetAll(str(blurbID))[0]
		
		if blurb:
			data = blurb
			# convert markdown
			data['content'] = markdown.markdown(data['content'][1:-1].replace('\\n','\n'))
		else:
			data = {
				'content': 'This Blurb Does Not Exist',
				'metadata': '',
				'blurbID': 'No Blurb Here'
			}
		
	except Exception as e:
		resp = jsonify({
			'status': 400,
			'error': 'Error in getBlurbByID controller: ' + str(e)
		})

		return resp
	
	dataType = request.args.get('dataType')
	
	if dataType == 'json':
		return Response(json.dumps(data), mimetype="text/json")
	else:
		return render_template('blurb.html', data=data)

# Get All Blurbs
def getBlurbs():

	# TODO: Better logging
	logging.warning('BlurbsAPI Call: getBlurb')

	# get objects
	data = services.BlurbService.GetAll()
	logging.warning(data)
	
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
	content = TextAreaField('content', [validators.Required()])
	
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
			'metadata': request.form.get('metadata'),
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
			logging.warning('No objected returned on save: 400')
			
			# return response object with error status code
			resp = jsonify({
				'status': 400,
				'error': 'Could not save submission'
			})

			resp.status_code = 400
			return resp	
	
	else:
		# FORM DATA IS INVALID
		logging.warning('Invalid form data: 400')

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
