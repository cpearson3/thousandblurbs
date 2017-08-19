import logging
from config import *
from util import *
#  Import supporting libs
from flask import Flask, render_template, redirect, request

from google.appengine.api import users

# Flask app app instance
app = Flask(__name__)

# thousandblurbs 0.1.0

# 301 Redirect *.appspot.com requests to custom domain if set
@app.before_request
def AppspotRedirect():

	if CUSTOM_DOMAIN == '':
		logging.warning('no custom domain set')
		return
	
	domain = request.headers['Host'].split(':')[0]
	logging.warning('request host domain: ' + domain)
	
	if domain == APPENGINE_DOMAIN:
		
		redirect_url = CUSTOM_DOMAIN + request.script_root + request.path
		logging.warning('redirecting to: ' + redirect_url)

		return redirect(redirect_url, code=301)

# URL Routes
@app.route('/', defaults={'path': ''})
def IndexController(path):
	# Return index
	data = initPageData()
	return render_template('index.html', data=data)
	
# Logout handler
@app.route('/logout')
@app.route('/logout/')
def LogoutController():
	return redirect(users.create_logout_url('/'))

# 404 handler	
@app.errorhandler(404)
def page_not_found(e):
	data = initPageData()
	return render_template('404.html', data=data), 404
	
# 500 handler	
@app.errorhandler(500)
def server_error(e):
	data = initPageData()
	return render_template('500.html', data=data), 500