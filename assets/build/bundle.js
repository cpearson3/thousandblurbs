(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
'use strict';

var _admin = require('./admin.ui');

var _dashboard = require('./dashboard.view');

var _namespace = require('./namespace.view');

var _submissions = require('./submissions.view');

var _submissions2 = require('./submissions.list');

var _namespace2 = require('./namespace.add');

// initialize UI
/* global angular */

(0, _admin.initUI)();

var app = angular.module('AdminApp', ['jsonFormatter', 'googlechart']);

app.controller('DashboardController', _dashboard.DashboardController);
app.controller('ViewSubmissionController', _submissions.ViewSubmissionController);
app.controller('ListSubmissionController', _submissions2.ListSubmissionController);
app.controller('AddNamespaceController', _namespace2.AddNamespaceController);
app.controller('ViewNamespaceController', _namespace.ViewNamespaceController);

},{"./admin.ui":2,"./dashboard.view":3,"./namespace.add":4,"./namespace.view":5,"./submissions.list":6,"./submissions.view":7}],2:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.initUI = initUI;
/* Initialize Materialize UI */

/* global $ */

function initUI() {

    // Initialize collapse button
    $(".button-collapse").sideNav({
        //edge: 'right'
    });
}

},{}],3:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, "__esModule", {
	value: true
});
exports.DashboardController = DashboardController;
/* DashboardController */

/* global $ */
/* global angular */
/* global location */
/* global vex */

function DashboardController($scope) {

	console.log('in the dashboard');

	$scope.submissions = [];
	$scope.namespaceIDs = [];
	$scope.formIDs = [];
	$scope.namespaceSubmissions = {};
	$scope.noSubmissions = false;

	$scope.myChartObject = {
		type: 'ColumnChart'
	};

	$.get('/_api/forms/').done(function (result) {
		console.log(result);

		if (result.length > 0) {
			$scope.submissions = result;

			$('#chart-container').show();

			for (var i = 0; i < result.length; i++) {
				var v_id = result[i]['namespaceID'];
				console.log(v_id);

				if ($scope.namespaceIDs.includes(v_id)) {
					// increment counter
					$scope.namespaceSubmissions[v_id] = $scope.namespaceSubmissions[v_id] + 1;
				} else {
					// add to list
					$scope.namespaceIDs.push(v_id);
					$scope.namespaceSubmissions[v_id] = 1;
				}
			}

			// set up row data array
			var rowData = [];

			for (var i in $scope.namespaceSubmissions) {
				var o = $scope.namespaceSubmissions[i];
				rowData.push({
					c: [{ v: i }, { v: o }]
				});
			}

			// set up chart
			$scope.myChartObject.data = {
				"cols": [{ id: "t", label: "Namespace ID", type: "string" }, { id: "s", label: "Submissions", type: "number" }],
				"rows": rowData
			};
		} else {
			$('#no-chart-data').show();
		}
	}).fail(function (result) {
		console.log('Dashboard Error: Could not retrieve form submissions');
	});
}

},{}],4:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, "__esModule", {
	value: true
});
exports.AddNamespaceController = AddNamespaceController;
/* AddNamespaceController */

/* global $ */
/* global angular */
/* global location */
/* global vex */

function AddNamespaceController($scope) {

	$scope.data = {
		namespaceID: '',
		description: ''
	};

	$scope.key = window.uQuery('key');

	// submit namepsace data
	$scope.submit = function () {

		console.log($scope.data);

		if ($scope.data.description == '' || $scope.data.namespaceID == '') {
			vex.dialog.alert('Enter a value for all fields');
			return;
		}

		$.post('/_api/namespace/save', $scope.data).done(function (result) {
			console.log('The data was saved.');
			console.log(result);
			vex.dialog.alert({
				'message': 'Namespace has been saved',
				'callback': function callback() {
					window.location = '/admin/namespace/';
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

},{}],5:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, "__esModule", {
	value: true
});
exports.ViewNamespaceController = ViewNamespaceController;
/* View Namespace controller */

/* global $ */
/* global angular */
/* global location */
/* global vex */

function ViewNamespaceController($scope, $timeout) {
	console.log('viewing namespaces');

	$scope.delete = function (namespace_key) {
		vex.dialog.confirm({
			message: 'Are you sure you want to delete this namespace?',
			callback: function callback(val) {
				if (val) {
					console.log('yes: ' + namespace_key);

					var data = {
						key: namespace_key
					};

					$.post('/_api/namespace/delete', data).done(function (result) {
						console.log(result);
						//location.href = location.href;
						vex.dialog.alert({
							message: 'Namespace deleted.',
							callback: function callback() {
								window.location = '/admin/namespace/';
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

},{}],6:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, "__esModule", {
	value: true
});
exports.ListSubmissionController = ListSubmissionController;
/* ListSubmissionController */

/* global $ */
/* global angular */
/* global location */
/* global vex */

function ListSubmissionController($scope, $timeout) {
	console.log('list form submissions');
}

},{}],7:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, "__esModule", {
	value: true
});
exports.ViewSubmissionController = ViewSubmissionController;
/* View Submission controller */

/* global $ */
/* global angular */
/* global location */
/* global vex */

function ViewSubmissionController($scope, $timeout) {
	console.log('viewing form submissions');

	$scope.delete = function (submission_key) {
		vex.dialog.confirm({
			message: 'Are you sure you want to delete this submission?',
			callback: function callback(val) {
				if (val) {
					console.log('yes: ' + submission_key);

					var data = {
						key: submission_key
					};

					$.post('/_api/forms/delete', data).done(function (result) {
						console.log(result);
						//location.href = location.href;
						vex.dialog.alert({
							message: 'Form Submission deleted.',
							callback: function callback() {
								window.location = '/admin/forms/';
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

},{}]},{},[1]);
