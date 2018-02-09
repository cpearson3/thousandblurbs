# Thousandblurbs Admin

from .. import util

#  Import supporting libs
from flask import Flask, render_template, url_for, request, jsonify
import logging

# Flask app app instance
app = Flask(__name__)

# Admin Dashboard controller
@app.route('/admin/<path:url>')
@app.route('/admin/')
def IndexController(url = None):

	# get objects
	data = util.initPageData()
	data['url_root'] = request.url_root
	return render_template('vue-app.html', data=data)
	
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
