import logging

# Forms Controllers

from .. import config
from .. import util

#  Import supporting libs
from flask import Flask, render_template, url_for, request, jsonify

from .. import services

# Form Component Controllers

# List Forms controller
def ListFormsController():
	# get objects
	submissions = services.FormService.GetAll()

	data = util.initPageData()
	data['submissions'] = submissions if submissions else []
	
	return render_template('list-submission.html', data=data)

# edit controller
def EditFormController():
	
	data = util.initPageData()

	try:
		key = request.args.get('key')

		util.copyDict(data, services.FormService.Get(key))

	except:
		# return empty dictionary if no key is passed
		pass

	return render_template('edit-submission.html', data=data)

# view controller
def ViewFormController():
	
	data = util.initPageData()
	
	try:
		key = request.args.get('key')

		util.copyDict(data, services.FormService.Get(key))
		
		logging.warning('got key')
		
	except Exception as e:
		
		logging.warning('Error: ' + str(e))

	return render_template('view-submission.html', data=data)