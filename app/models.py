# models.py
import logging
from google.appengine.ext import ndb

def fromEntity(ent):
	obj = {}
	for i in ent.keys():
		obj[i] = ent[i]
	return obj

# Extend ndb.Model class
class Model(ndb.Model):
	# in convert dictionary to this
	def fromDict(self, data):
		for name, value in data.iteritems():
			n = name
			try:
				# ignore key
				if n == "key":
					continue
				if n == "_key":
					continue
				if n[:1] == '_':
					n = n[1:]
			except:
				pass
			setattr(self, n, value)
	
	# Returns Dictionary of data
	@staticmethod
	def toDict(obj):
		try:
			objData = fromEntity(obj._entity)
			objData['key'] = str(obj.key())
			return objData
		except Exception as e:
			logging.warning('error: ' + str(e))
			return 0	
			
	@staticmethod
	def listToDict(l):
		try:
			list = []
			for i in l:
				objData = fromEntity(i._entity)
				objData['key'] = str(i.key())
				list.append(objData)
			return list
		except:
			return 0

# Namespace Model
class Namespace(Model):
	namespaceID = ndb.StringProperty()
	description = ndb.TextProperty()
	datetime = ndb.DateTimeProperty(auto_now_add=True)

# Form Submission Model
class FormSubmission(Model):
	formID = ndb.StringProperty()
	namespaceID = ndb.StringProperty()
	data = ndb.TextProperty()
	clientIP = ndb.StringProperty()
	datetime = ndb.DateTimeProperty(auto_now_add=True)

# Blurb Model
class Blurb(Model):
	blurbID = ndb.StringProperty()
	namespaceID = ndb.StringProperty()
	content = ndb.TextProperty()
	metadata = ndb.TextProperty()
	datetime = ndb.DateTimeProperty(auto_now_add=True)