# Thousandblurbs Admin

from .. import config
from .. import util

#from config import *
#from util import *

#  Import supporting libs
from flask import Flask, render_template, url_for, request, jsonify
import logging

# import upload services
from .. import services
from namespace import *
from forms import *
from blurbs import *

# Flask app app instance
app = Flask(__name__)


# Admin Dashboard controller
@app.route('/admin/')
def IndexController():

	# get objects
	submissions = services.FormService.GetAll()

	data = util.initPageData()
	data['submissions'] = submissions if submissions else []
	
	return render_template('dashboard.html', data=data)
	
# Settings controller
@app.route('/admin/settings/')
def SettingsController():

	# get objects
	#submissions = FormService.GetAll()

	data = util.initPageData()
	return render_template('settings.html', data=data)
	
# 404 handler	
@app.errorhandler(404)
def page_not_found(e):
	data = util.initPageData()
	return render_template('404.html', data=data), 404
	
# 500 handler	
@app.errorhandler(500)
def server_error(e):
	data = util.initPageData()
	return render_template('500.html', data=data), 500
	
# Define Data Controllers
app.add_url_rule('/admin/namespace/',  view_func=ListNamespaceController)
app.add_url_rule('/admin/namespace/view',  view_func=ViewNamespaceController)
app.add_url_rule('/admin/namespace/add',  view_func=AddNamespaceController)

app.add_url_rule('/admin/forms/',  view_func=ListFormsController)
app.add_url_rule('/admin/forms/view',  view_func=ViewFormController)
app.add_url_rule('/admin/forms/edit',  view_func=EditFormController)

app.add_url_rule('/admin/blurbs/',  view_func=ListBlurbsController)
app.add_url_rule('/admin/blurbs/view',  view_func=ViewBlurbController)
app.add_url_rule('/admin/blurbs/add',  view_func=AddBlurbController)