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
		for i in query.iter():
			obj = {
				'key': i.key.urlsafe(),
				'description': i.description,
				'namespaceID': i.namespaceID,
				'datetime': str(i.datetime)
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
		
		for i in query.iter():
			result.append(str(i.namespaceID))

		return result

	except Exception as e:
		# handle error on get
		logging.warning('NamespaceService.GetAllIDs error: ' + str(e))
		return None

# get by key
def Get(key):

	try:
		# get by key
		i =  ndb.Key(urlsafe=key).get()
		result = {
			'key': i.key.urlsafe(),
			'description': i.description,
			'namespaceID': i.namespaceID,
			'datetime': str(i.datetime),
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
		i =  ndb.Key(urlsafe=key).get()
		
		i.key.delete()
		
		return True

	except Exception as e:
		# handle error on get
		logging.warning('NamespaceService.Delete error: ' + str(e))
		return None