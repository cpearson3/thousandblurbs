/* AddNamespaceController */

/* global $ */
/* global angular */
/* global location */
/* global vex */

export function AddNamespaceController($scope) {

	$scope.data = {
		namespaceID: '',
		description: ''
	}
	
	$scope.key = window.uQuery('key');

	// submit namepsace data
	$scope.submit = function() {
		
		console.log($scope.data);
		
		if (($scope.data.description == '') || ($scope.data.namespaceID == '')) {
			vex.dialog.alert('Enter a value for all fields');
			return;
		}
 
		$.post('/_api/namespace/save', $scope.data)
		.done(function(result) {
			console.log('The data was saved.');
			console.log(result);
			vex.dialog.alert({
				'message': 'Namespace has been saved',
				'callback': function() {
					window.location = '/admin/namespace/';
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