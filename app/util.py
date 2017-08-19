# Global functions
from config import *

def copyDict(a, b):
	for iKey in b.keys():
		a[iKey] = b[iKey]
	
	return

def initPageData():
	return {
		'context': SITE_CONTEXT
	}
