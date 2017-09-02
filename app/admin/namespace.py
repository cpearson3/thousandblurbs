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
    namespace = {}
    
    try:
        key = request.args.get('key')
        namespaceID = request.args.get('namespaceID')
        
        # is key passed
        if key:
            logging.warning('Key Passed: ' + str(key))
            namespace = services.NamespaceService.Get(key=key)
        else:
            if namespaceID:
                logging.warning('NamespaceID Passed: ' + str(namespaceID))
                namespace = services.NamespaceService.Get(namespaceID=namespaceID)
        
        util.copyDict(data, namespace)

    except Exception as e:
    
        logging.warning('Error: ' + str(e))
		
    return render_template('view-namespace.html', data=data)
    
# Add Controller
def AddNamespaceController():
    data = util.initPageData()
    
    return render_template('add-namespace.html', data=data)