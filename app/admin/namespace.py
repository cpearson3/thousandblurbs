# Namespace Controllers
from .. import config
from .. import util

#from config import *
#from util import *

#  Import supporting libs
from flask import Flask, render_template, url_for, request, jsonify
from .. import services

import logging

# List Namespaces controller
def ListNamespaceController():

	# get objects
	submissions = services.NamespaceService.GetAll()

	data = util.initPageData()
	data['namespaces'] = submissions if submissions else []
	
	return render_template('list-namespace.html', data=data)
	
# View Controller
def ViewNamespaceController():
    data = util.initPageData()
    
    try:
        key = request.args.get('key')
        
        util.copyDict(data, services.NamespaceService.Get(key))
        
        logging.warning('got key')
    
    except Exception as e:
    
        logging.warning('Error: ' + str(e))
		
    return render_template('view-namespace.html', data=data)
    
# Add Controller
def AddNamespaceController():
    data = util.initPageData()
    
    return render_template('add-namespace.html', data=data)