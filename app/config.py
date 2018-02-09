# Thousandblurbs 
# Global site configuration

HOST = ""
APPENGINE_DOMAIN = ""
API_KEY = ""
ALLOWED_DOMAINS = '*'
ADMIN_EMAIL = ""
SEND_NOTIFICATIONS = False

# Global context for page templates
SITE_CONTEXT = {
	'api_key': API_KEY,
	'allowed_domains': ALLOWED_DOMAINS,
	'admin_email': ADMIN_EMAIL,
	'send_notification': SEND_NOTIFICATIONS,
	'host': HOST
}
