# Thousandblurbs 

# Global site configuration

API_KEY = ""
ALLOWED_DOMAINS = '*'
ADMIN_EMAIL = ""
SEND_NOTIFICATIONS = False

APP_VERSION = "0.3.4"

SITE_TITLE = "Thousandblurbs"
SITE_DESCRIPTION = "Open Source Cloud Advertising Platform"
NAV_TITLE = "Thousandblurbs"

# Domain information
# Replace with your Google App Engine project ID
APPENGINE_DOMAIN = ''
CUSTOM_DOMAIN = ''

# Global context for page templates
SITE_CONTEXT = {
	'api_key': API_KEY,
	'allowed_domains': ALLOWED_DOMAINS,
	'title': SITE_TITLE,
	'description': SITE_DESCRIPTION,
	'image': '',
	'nav_title': NAV_TITLE,
	'app_version': APP_VERSION
}
