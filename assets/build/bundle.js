(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
'use strict';

var _adminController = require('./adminController');

var _editController = require('./editController');

/* global angular */

var app = angular.module('AdminApp', ['jsonFormatter']);

app.controller('AdminController', _adminController.AdminController);
app.controller('EditController', _editController.EditController);

},{"./adminController":2,"./editController":3}],2:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, "__esModule", {
	value: true
});
exports.AdminController = AdminController;
/* Admin controller */

/* global $ */
/* global angular */
/* global location */
/* global vex */

function AdminController($scope, $timeout) {
	console.log('in the dashboard');

	$scope.delete = function (submission_key) {
		vex.dialog.confirm({
			message: 'Are you sure you want to delete this contact',
			callback: function callback(val) {
				if (val) {
					console.log('yes: ' + submission_key);

					var data = {
						key: submission_key
					};

					$.post('/_api/v1/delete/', data).done(function (result) {
						console.log(result);
						//location.href = location.href;
						vex.dialog.alert({
							message: 'Contact deleted. Refreshing page',
							callback: function callback() {
								$timeout(function () {
									location.reload(true);
								}, 300);
							}
						});
					}).fail(function (result) {
						console.log(result);
						vex.dialog.alert('Could not delete item');
					});
				} else {
					console.log('i see you do not want to delete this.');
				}
			}
		});
	};
}

},{}],3:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, "__esModule", {
	value: true
});
exports.EditController = EditController;
/* Edit Controller */

/* global $ */
/* global angular */
/* global location */
/* global vex */

function EditController($scope) {

	$scope.key = window.uQuery('key');

	// submit contact form
	$scope.submit = function (e) {

		var formElement = angular.element(e.target);

		var data = {
			data: $('#data').val(),
			key: $scope.key
		};

		$.post('/_api/v1/save/', data).done(function (result) {
			console.log('The data was saved.');
			console.log(result);
			vex.dialog.alert({
				'message': 'Submission has been saved',
				'callback': function callback() {
					location.href = '/admin/';
				}
			});
		}).fail(function (result) {
			vex.dialog.alert({
				'message': 'An error occurred: ' + result,
				'callback': function callback() {
					console.log('An error has occurred:');
					console.log(result);
				}
			});
		});

		return;
	};
}

},{}]},{},[1]);
