import logging
from config import *

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
@app.route('/<path>/')
def PageController(path):

	# thousandblurbs 0.1.0
	
	# Get URL routes from global pages dictionary
	site_paths = SITE_PAGES.keys()
	
	if path in site_paths:
		
		# Get the global context and set SEO Fields
		context = SITE_CONTEXT
		context['base_url'] = request.url
		context['description'] = SITE_PAGES[path]['description']
		context['title'] = SITE_PAGES[path]['title']
		
		# Render page template
		return render_template(path+'.html',post=context)
		
	elif path == '':
		
		# BUG?: context must be explicitly set
		context = SITE_CONTEXT
		context['title'] = SITE_TITLE
		context['description'] = SITE_DESCRIPTION
		
		# Return index
		return render_template('index.html',post=context)
	else:
		# Return 404
		return render_template('404.html', post=SITE_CONTEXT), 404
	
# Logout handler
@app.route('/logout')
@app.route('/logout/')
def LogoutController():
	return redirect(users.create_logout_url('/'))

# 404 handler	
@app.errorhandler(404)
def page_not_found(e):

	return render_template('404.html', post=SITE_CONTEXT), 404
	
# 500 handler	
@app.errorhandler(500)
def server_error(e):
	return render_template('500.html', post=SITE_CONTEXT), 500