# Thousandblurbs
Thousandblurbs is a web application starter kit built for the cloud using Google App Engine, Python and Flask.

## Features include:

* API to capture, store, and retrieve form data using Google App Engine and the Cloud Datastore
* Control user access using Google Cloud management
* Segment data into namespaces to accomodate for multiple data sources
* Export captured data as a CSV file
* Form capture service and maintenance using Google Cloud Datastore

## Changelog

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