from google.appengine.api import mail, users, app_identity
from flask import render_template, request, jsonify

import logging

def sendNotification(data={}):
    logging.warning('sendNotication Called')
    
    try:
        content = render_template('notification.html', data=data)
        sender = '{}@appspot.gserviceaccount.com'.format(
            app_identity.get_application_id()
        )
        
        mail.send_mail(sender=sender,
            to=sender,
            subject="Form Submission Notification",
            body=content
        )
        
        logging.warning('Successly sent notification')
        return content
    except Exception as e:
        logging.warning('Exception: ' + str(e))
        return None
    
    return True