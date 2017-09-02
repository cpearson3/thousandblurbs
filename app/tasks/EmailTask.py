import logging

#  Import supporting libs
from flask import render_template, request, jsonify

def Notification():
    logging.warning('Email Notication Controller Called')
    
    data = {}
    
    try:
        for i in request.form.keys():
			data[i] = request.form.get(i)
			
        logging.warning('Data: ' + str(data))
        
    except Exception as e:
		# Oh no, something went wrong
		# return response object with error status code
		logging.warning('Exception: ' + str(e))
		resp = jsonify({
			'status': 400,
			'error': str(e)
		})

		resp.status_code = 400
		return resp	
    
    resp = jsonify(data)
    resp.status_code = 200
    return resp