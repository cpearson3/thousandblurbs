/* AddBlurbController */

/* global $ */
/* global angular */
/* global location */
/* global vex */

export function AddBlurbController($scope) {

	$scope.data = {
		namespaceID: '',
		blurbID: '',
		content: ''
	}
	
	$scope.key = window.uQuery('key');

	// submit namepsace data
	$scope.submit = function() {
		
		console.log($scope.data);
		
		if (($scope.data.content == '') || ($scope.data.namespaceID == '') || ($scope.data.blurbID == '')) {
			vex.dialog.alert('Enter a value for all fields');
			return;
		}
 
		$.post('/_api/blurbs/save', $scope.data)
		.done(function(result) {
			console.log('The data was saved.');
			console.log(result);
			vex.dialog.alert({
				'message': 'Blurb has been saved',
				'callback': function() {
					window.location = '/admin/blurbs/';
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