# Form Service
# similar to the angular pattern, put data services here

from google.appengine.ext import ndb
from .. import models

import NamespaceService

import json
import logging

def GetAll(formID = None, namespaceID = None):
	"""
	Get All Method
	Args:
	    formID (str): Form ID (optional)
	Returns:
	    list: List of dictionaries retrieved from Data Store. None otherwise
	"""
	
	try:
		# build result list
		result = []
		
		query = None
		
		# is formID passed
		if formID:
			query = models.FormSubmission.query(models.FormSubmission.formID == formID).order(-models.FormSubmission.datetime)
		else:
			# is namespaceID passed
			if namespaceID:
				query = models.FormSubmission.query(models.FormSubmission.namespaceID == namespaceID).order(-models.FormSubmission.datetime)
			else:
				# get all, order by datetime
				query = models.FormSubmission.query().order(-models.FormSubmission.datetime)
		
		for i in query.iter():
			obj = {
				'key': i.key.urlsafe(),
				'data': i.data,
				'formID': i.formID,
				'namespaceID': i.namespaceID,
				'datetime': str(i.datetime),
				'clientIP': str(i.clientIP)
			}
			result.append(obj)

		return result

	except Exception as e:
		# handle error on get
		logging.warning('FormService.GetAll ERROR: ' + str(e))
		return None

# get by key
def Get(key):

	try:
		# get by key
		i =  ndb.Key(urlsafe=key).get()
		result = {
			'key': i.key.urlsafe(),
			'data': i.data,
			'formID': i.formID,
			'namespaceID': i.namespaceID,
			'datetime': str(i.datetime),
			'clientIP': i.clientIP
		}

		return result

	except Exception as e:
		# handle error on get
		logging.warning('FormService.Get ERROR: ' + str(e))
		return None

# Save Method
def Save(data):
	
	if 'formID' not in data:
		logging.warning('FormService.Save ERROR: no formID')
		return None
	
	if 'namespaceID' not in data:
		logging.warning('FormService.Save ERROR: no namespaceID')
		return None
		
	# validate namespace
	namespaces = NamespaceService.GetAllIDs()
	
	if namespaces:
		logging.warning('Namespace IDs Retrieved: ' + str(namespaces))
		
		if data['namespaceID'] not in namespaces:
			logging.warning('FormService.Save ERROR: Namespace %s is not valid' % (data['namespaceID']))
			return None
		
	else:
		logging.warning('FormService.Save ERROR: Could not retrieve namespace IDs')
		return None

	if 'key' in data:
		if data['key']:
			newObj = ndb.Key(urlsafe=data['key']).get()

			if newObj == None:
				logging.warning('Key not found, new object created')
				newObj = models.FormSubmission()
		else:
			newObj = models.FormSubmission()

	else:
		logging.warning('no key passed: creating new obj')
		newObj = models.FormSubmission()

	try:
		# save some data in a model
		newObj.data = json.dumps(data['data'])
		newObj.formID = data['formID']
		newObj.namespaceID = data['namespaceID']
		newObj.clientIP = data['clientIP']
		newObj.put()

		logging.warning('FormService.Save SUCCESS')
		
		data['datetime'] = newObj.datetime
		return data

	except Exception as e:
		# handle error on save
		logging.warning('FormService.Save ERROR: ' + str(e))
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
		logging.warning('FormService.Delete ERROR: ' + str(e))
		return None