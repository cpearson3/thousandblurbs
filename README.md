# Thousandblurbs
Thousandblurbs is a platform for creating and hosting HTML ads on Google App Engine

## Features include:

* Built with Python and Flask.
* Control access with Google Cloud user management tools.

## Changelog

### 0.4.0
Thousandblurbs is now focused solely on being an HTML ad platform.
Form submission code has been split into its own project ( [View on Github](https://github.com/cpearson3/appengine-form-capture) )

* Added iframe embed code to blurbs admin
* Blurb links now open in new window


### 0.3.4
* Added Blurbs - Responsive HTML Ads
** Add / View / List Admin Screens
** Get / Save / Delete API Functions

### 0.3.3
* Added Email Notification Service (Disabled by default. Can be enabled in config)

### 0.3.2
* Form Submissions can be viewed by Namespace and by Form ID
* Added navigational links between Namespace and Form Submission views
* Admin UI improvements

### 0.3.1
* Client IP address is now stored for all form submissions
* Added fixed action button to Admin UI

### 0.3.0
* New user interface built with the Materialize framework
* Added Namespaces to segment form submission data
* Added API key and field validation
* Added Google Charts to show submissions by namespace to the dashboard 
* Added configuration variables and a Settings view

### 0.2.0
* Added key check to form submission API
* Admin app is now built with ES6
* Updated gulpfile and dependent packages

### 0.1.0 
* Initial release

### 0.0.1
* Proof of concept