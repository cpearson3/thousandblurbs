# Global functions
from config import *

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
	context['user_email'] = user.email()
	
	return {
		'context': context
	}
