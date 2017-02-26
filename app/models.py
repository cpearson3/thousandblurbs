
# models.py
import logging
from google.appengine.ext import ndb

# Form Submission Model
class FormSubmission(ndb.Model):
	formID = ndb.StringProperty()
	data = ndb.TextProperty()
	datetime = ndb.DateTimeProperty(auto_now_add=True)
