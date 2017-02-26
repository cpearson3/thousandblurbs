# Form Service
# similar to the angular pattern, put data services here

from google.appengine.ext import ndb
from .. import models

import json
import logging

# Upload File Service
# Get All Method

def GetAll():
	try:
		# build result list
		result = []
		# get all, order by datetime
		query = models.FormSubmission.query().order(-models.FormSubmission.datetime)
		for i in query.iter():
			obj = {
				'key': i.key.urlsafe(),
				'data': i.data,
				'formID': i.formID,
				'datetime': i.datetime
			}
			result.append(obj)

		return result

	except Exception as e:
		# handle error on get
		logging.warning('FormService.GetAll error: ' + str(e))
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
			'datetime': i.datetime,
		}

		return result

	except Exception as e:
		# handle error on get
		logging.warning('FormService.Get error: ' + str(e))
		return None

# Save Method
def Save(data):
	
	if 'formID' not in data:
		return None

	if 'key' in data:
		if data['key']:
			newObj = ndb.Key(urlsafe=data['key']).get()

			if newObj == None:
				logging.warning('key not found, new object created')
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
		newObj.put()

		logging.warning('FormService.Save SUCCESS')
		return newObj.key

	except Exception as e:
		# handle error on save
		logging.warning('FormService.Save error: ' + str(e))
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
		logging.warning('FormService.Delete error: ' + str(e))
		return None