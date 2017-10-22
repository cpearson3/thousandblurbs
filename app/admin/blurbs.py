import logging

# Blurbs Controllers

from .. import config
from .. import util

#  Import supporting libs
from flask import Flask, render_template, url_for, request, jsonify

from .. import services

# Blurb Component Controllers

# List Blurbs controller
def ListBlurbsController():
	logging.warning('ListBlurbsController:')
	
	formID = request.args.get('formID')
	namespaceID = request.args.get('namespaceID')
	submisssions = []
	
	# is formID passed
	if formID:
		logging.warning('BlurbID passed: ' + str(formID))
		blurbs = services.BlurbService.GetAll(formID=formID)
	else:
		# is namespaceID passed
		if namespaceID:
			logging.warning('NamespaceID passed: ' + str(namespaceID))
			blurbs = services.BlurbService.GetAll(namespaceID=namespaceID)
		else:
			# get all
			blurbs = services.BlurbService.GetAll()

	data = util.initPageData()
	data['formID'] = formID
	data['namespaceID'] = namespaceID
	data['blurbs'] = blurbs if blurbs else []
	
	return render_template('list-blurb.html', data=data)

# add controller
def AddBlurbController():
	
	data = util.initPageData()
	
	try:
		
		data['namespaces'] = services.NamespaceService.GetAllIDs()
		logging.warning('Namespaces: ' + str(data['namespaces']))

	except Exception as e:
		
		logging.warning('Error: ' + str(e))

	return render_template('add-blurb.html', data=data)

# view controller
def ViewBlurbController():
	
	data = util.initPageData()
	
	try:
		key = request.args.get('key')

		util.copyDict(data, services.BlurbService.Get(key))
		
		logging.warning('got key')
		
	except Exception as e:
		
		logging.warning('Error: ' + str(e))

	return render_template('view-blurb.html', data=data)