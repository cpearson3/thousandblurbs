# Global functions
from config import *

import json
from google.appengine.api import users
	
def copyDict(a, b):
	# copy dictionary
	for iKey in b.keys():
		a[iKey] = b[iKey]
	
	return

def initPageData():
	
	# get site context
	context = SITE_CONTEXT
	
	# get current user
	user = users.get_current_user()
	if user:
		context['user_email'] = user.email()
	
	return {
		'context': context
	}

def json_accetable(s):
	return json.loads(s.replace('\\"', '\"').replace("'", "\"")[1:-1]) if s != None and s != "null" else ''