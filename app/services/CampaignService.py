# Campaign Service

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
		query = models.Campaign.query().order(-models.Campaign.datetime)
		for campaign in query.iter():
			obj = {
				'key': campaign.key.urlsafe(),
				'description': campaign.description,
				'campaignID': campaign.campaignID,
				'datetime': str(campaign.datetime)
			}
			result.append(obj)

		return result

	except Exception as e:
		# handle error on get
		logging.warning('CampaignService.GetAll error: ' + str(e))
		return None

# get all campaignIDs
def GetAllIDs():
	try:
		# build result list
		result = []
		# get all, order by datetime
		query = models.Campaign.query()
		
		for campaign in query.iter():
			result.append(str(campaign.campaignID))

		return result

	except Exception as e:
		# handle error on get
		logging.warning('CampaignService.GetAllIDs error: ' + str(e))
		return None

# get by key
def Get(key=None, campaignID=None):

	campaign = None
	try:
		if key: 
			# get by key
			campaign =  ndb.Key(urlsafe=key).get()
			
		else:
			if campaignID:
				query = models.Campaign.query(models.Campaign.campaignID == campaignID).order(models.Campaign.datetime)
				# get last result from query
				for obj in query.iter():
					campaign = obj
			else:
				# required arguments not passed
				return None
			
		result = {
				'key': campaign.key.urlsafe(),
				'description': campaign.description,
				'campaignID': campaign.campaignID,
				'datetime': str(campaign.datetime),
			}

		return result

	except Exception as e:
		# handle error on get
		logging.warning('CampaignService.Get error: ' + str(e))
		return None

# Save Method
def Save(data):
	
	if 'campaignID' not in data:
		return None

	if 'key' in data:
		if data['key']:
			newObj = ndb.Key(urlsafe=data['key']).get()

			if newObj == None:
				logging.warning('key not found, new object created')
				newObj = models.Campaign()
		else:
			newObj = models.Campaign()

	else:
		logging.warning('no key passed: creating new obj')
		newObj = models.Campaign()

	try:
		# save some data in a model
		newObj.description = data['description']
		newObj.campaignID = data['campaignID']
		newObj.put()

		logging.warning('CampaignService.Save SUCCESS')
		return newObj.key

	except Exception as e:
		# handle error on save
		logging.warning('CampaignService.Save error: ' + str(e))
		return None

# Delete Method
def Delete(key):
	try:
		# get by key
		campaign =  ndb.Key(urlsafe=key).get()
		
		campaign.key.delete()
		
		return True

	except Exception as e:
		# handle error on get
		logging.warning('CampaignService.Delete error: ' + str(e))
		return None