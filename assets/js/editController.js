/* Edit Controller */

/* global $ */
/* global angular */
/* global location */
/* global vex */

export function EditController($scope) {

	$scope.key = window.uQuery('key');

	// submit contact form
	$scope.submit = function(e) {

		var formElement = angular.element(e.target);

		var data = {
			data: $('#data').val(),
			key: $scope.key	
		};		

		$.post('/_api/v1/save/', data)
		.done(function(result) {
			console.log('The data was saved.');
			console.log(result);
			vex.dialog.alert({
				'message': 'Submission has been saved',
				'callback': function() {
					location.href = '/admin/';
				}	
			});
			
		})
		.fail(function(result) {
			vex.dialog.alert({
				'message': 'An error occurred: ' + result,
				'callback': function() {
					console.log('An error has occurred:');
					console.log(result);
				}
			})
			
		});

		return;
	};
}