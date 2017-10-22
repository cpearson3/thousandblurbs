from google.appengine.api import mail, users, app_identity
from flask import render_template, request, jsonify

import logging

from .. import config

def submissionEmail(data):
	return """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Form Submission Notification</title>
</head>
<body>
  <h1>Form Submission Notification</h1>
  <p>Namespace ID: {namespaceID} </p>
  <p>Form ID: {formID}</p>
  <p>Date / Time: {datetime}</p>
  <p>Data:</p>
  <p>{data}</p>
</body>
</html>	
		""".format(namespaceID=data['namespaceID'], formID=data['formID'], datetime=data['datetime'], data=data['data'])

# send notification
def sendNotification(content):
	logging.warning('sendNotication Called')

	try:
		logging.warning('Rendering Email Template')

		# content = submissionEmail(data)

		logging.warning('Sending notification email')
		mail.send_mail(sender=config.ADMIN_EMAIL,
			to=config.ADMIN_EMAIL,
			subject="Form Submission Notification",
			body=content
		)
		logging.warning('Mail sent')
	except Exception as e:
		logging.warning('Exception: ' + str(e))
		return None

	return True