# Thousandblurbs 

# Global site configuration

API_KEY = ""
ALLOWED_DOMAINS = '*'

APP_VERSION = "0.3.0"
SITE_TITLE = "Serve Dynamic Web Components with Thousandblurbs"
SITE_DESCRIPTION = "Your web data backend on Google App Engine."
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
