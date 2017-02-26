# thousandblurbs 0.1.0

# Global site configuration

SITE_TITLE = "A Web Application Starter Kit | Thousandblurbs"
SITE_DESCRIPTION = "Thousandblurbs is a web application starter kit built for the cloud using Google App Engine, Flask, and Bootsmooth."
NAV_TITLE = "Thousandblurbs"

# Contact information
YOURNAME = ""
YOUREMAIL = ""

# Domain information
# Replace with your Google App Engine project ID
APPENGINE_DOMAIN = 'thousandblurbs.appspot.com'
CUSTOM_DOMAIN = 'https://thousandblurbs.com'

# Global context for page templates
SITE_CONTEXT = {
	'title': SITE_TITLE,
	'description': SITE_DESCRIPTION,
	'image': '',
	'nav_title': NAV_TITLE,
}

# URL Routes and SEO Fields
# Example:
# SITE_PAGES = {
#	'about': {
#		'title': 'About the PACE Project, a West Virginia Non-Profit Organization',
#		'description': 'Learn more about The PACE Project, a Non-Profit Organization based in Fairmont, WV.'
#	}
#}

SITE_PAGES = {}