# models.py
import logging
from google.appengine.ext import ndb

# Namespace Model
class Namespace(ndb.Model):
	namespaceID = ndb.StringProperty()
	description = ndb.TextProperty()
	datetime = ndb.DateTimeProperty(auto_now_add=True)

# Form Submission Model
class FormSubmission(ndb.Model):
	formID = ndb.StringProperty()
	namespaceID = ndb.StringProperty()
	data = ndb.TextProperty()
	clientIP = ndb.StringProperty()
	datetime = ndb.DateTimeProperty(auto_now_add=True)
