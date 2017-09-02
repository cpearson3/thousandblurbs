# Namespace Service
# similar to the angular pattern, put data services here

from google.appengine.ext import ndb
from .. import models

import json
import logging

# Get All Method

def GetAll():
	try:
		# build result list
		result = []
		# get all, order by datetime
		query = models.Namespace.query().order(-models.Namespace.datetime)
		for namespace in query.iter():
			obj = {
				'key': namespace.key.urlsafe(),
				'description': namespace.description,
				'namespaceID': namespace.namespaceID,
				'datetime': str(namespace.datetime)
			}
			result.append(obj)

		return result

	except Exception as e:
		# handle error on get
		logging.warning('NamespaceService.GetAll error: ' + str(e))
		return None

# get all namespaceIDs
def GetAllIDs():
	try:
		# build result list
		result = []
		# get all, order by datetime
		query = models.Namespace.query()
		
		for namespace in query.iter():
			result.append(str(namespace.namespaceID))

		return result

	except Exception as e:
		# handle error on get
		logging.warning('NamespaceService.GetAllIDs error: ' + str(e))
		return None

# get by key
def Get(key=None, namespaceID=None):

	namespace = None
	try:
		if key: 
			# get by key
			namespace =  ndb.Key(urlsafe=key).get()
			
		else:
			if namespaceID:
				query = models.Namespace.query(models.Namespace.namespaceID == namespaceID).order(models.Namespace.datetime)
				# get last result from query
				for obj in query.iter():
					namespace = obj
			else:
				# required arguments not passed
				return None
			
		result = {
				'key': namespace.key.urlsafe(),
				'description': namespace.description,
				'namespaceID': namespace.namespaceID,
				'datetime': str(namespace.datetime),
			}

		return result

	except Exception as e:
		# handle error on get
		logging.warning('NamespaceService.Get error: ' + str(e))
		return None

# Save Method
def Save(data):
	
	if 'namespaceID' not in data:
		return None

	if 'key' in data:
		if data['key']:
			newObj = ndb.Key(urlsafe=data['key']).get()

			if newObj == None:
				logging.warning('key not found, new object created')
				newObj = models.Namespace()
		else:
			newObj = models.Namespace()

	else:
		logging.warning('no key passed: creating new obj')
		newObj = models.Namespace()

	try:
		# save some data in a model
		newObj.description = data['description']
		newObj.namespaceID = data['namespaceID']
		newObj.put()

		logging.warning('NamespaceService.Save SUCCESS')
		return newObj.key

	except Exception as e:
		# handle error on save
		logging.warning('NamespaceService.Save error: ' + str(e))
		return None

# Delete Method
def Delete(key):
	try:
		# get by key
		namespace =  ndb.Key(urlsafe=key).get()
		
		namespace.key.delete()
		
		return True

	except Exception as e:
		# handle error on get
		logging.warning('NamespaceService.Delete error: ' + str(e))
		return None