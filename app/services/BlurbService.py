
# Blrub Service
# similar to the angular pattern, put data services here

from google.appengine.ext import ndb
from .. import models

import NamespaceService

import json
import logging

def GetAll(blurbID = None, namespaceID = None):
	"""
	Get All Method
	Args:
	    blurbID (str): Blurb ID (optional)
	Returns:
	    list: List of dictionaries retrieved from Data Store. None otherwise
	"""
	
	try:
		# build result list
		result = []
		
		query = None
		
		# is blurbID passed
		if blurbID:
			query = models.Blurb.query(models.Blurb.blurbID == blurbID).order(-models.Blurb.datetime)
		else:
			# is namespaceID passed
			if namespaceID:
				query = models.Blurb.query(models.Blurb.namespaceID == namespaceID).order(-models.Blurb.datetime)
			else:
				# get all, order by datetime
				query = models.Blurb.query().order(-models.Blurb.datetime)
		
		for i in query.iter():
			obj = {
				'key': i.key.urlsafe(),
				'content': i.content,
				'blurbID': i.blurbID,
				'namespaceID': i.namespaceID,
				'datetime': str(i.datetime),
			}
			result.append(obj)

		return result

	except Exception as e:
		# handle error on get
		logging.warning('BlurbService.GetAll ERROR: ' + str(e))
		return None

# get by key
def Get(key):

	try:
		# get by key
		i =  ndb.Key(urlsafe=key).get()
		result = {
			'key': i.key.urlsafe(),
			'content': i.content,
			'blurbID': i.blurbID,
			'namespaceID': i.namespaceID,
			'datetime': str(i.datetime),
		}

		return result

	except Exception as e:
		# handle error on get
		logging.warning('BlurbService.Get ERROR: ' + str(e))
		return None

# Save Method
def Save(data):
	
	if 'blurbID' not in data:
		logging.warning('BlurbService.Save ERROR: no blurbID')
		return None
	
	if 'namespaceID' not in data:
		logging.warning('BlurbService.Save ERROR: no namespaceID')
		return None
		
	# validate namespace
	namespaces = NamespaceService.GetAllIDs()
	
	if namespaces:
		logging.warning('Namespace IDs Retrieved: ' + str(namespaces))
		
		if data['namespaceID'] not in namespaces:
			logging.warning('BlurbService.Save ERROR: Namespace %s is not valid' % (data['namespaceID']))
			return None
		
	else:
		logging.warning('BlurbService.Save ERROR: Could not retrieve namespace IDs')
		return None

	if 'key' in data:
		if data['key']:
			newObj = ndb.Key(urlsafe=data['key']).get()

			if newObj == None:
				logging.warning('Key not found, new object created')
				newObj = models.Blurb()
		else:
			newObj = models.Blurb()

	else:
		logging.warning('no key passed: creating new obj')
		newObj = models.Blurb()

	try:
		# save some data in a model
		newObj.content = json.dumps(data['content'])
		newObj.blurbID = data['blurbID']
		newObj.namespaceID = data['namespaceID']
		newObj.put()

		logging.warning('BlurbService.Save SUCCESS')
		
		data['datetime'] = newObj.datetime
		return data

	except Exception as e:
		# handle error on save
		logging.warning('BlurbService.Save ERROR: ' + str(e))
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
		logging.warning('BlurbService.Delete ERROR: ' + str(e))
		return None