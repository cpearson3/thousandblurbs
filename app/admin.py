# Thousandblurbs Admin
from config import *

#  Import supporting libs
from flask import Flask, render_template, url_for, request, jsonify

# import upload services
from services import FormService

import logging

# Flask app app instance
app = Flask(__name__)

# admin controller
@app.route('/admin/')
def IndexController():

	# get objects
	submissions = FormService.GetAll()

	data = {}
	data['submissions'] = submissions if submissions else []
	return render_template('admin/admin.html', data=data)

# edit controller
@app.route('/admin/edit')
def EditController():

	try:
		key = request.args.get('key')

		data = FormService.Get(key) 
	except:
		# return empty dictionary if no key is passed
		data = {}

	return render_template('admin/edit.html', data=data)

# view controller
@app.route('/admin/view')
def ViewController():

	try:
		key = request.args.get('key')

		data = FormService.Get(key) 
		logging.warning('got key')
	except:
		
		data = {}
		logging.warning('NO key')

	return render_template('admin/view.html', data=data)
