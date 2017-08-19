/* View Submission controller */

/* global $ */
/* global angular */
/* global location */
/* global vex */

export function ViewSubmissionController($scope, $timeout) {
	console.log('viewing form submissions');

	$scope.delete = function(submission_key) {
		vex.dialog.confirm({
			message: 'Are you sure you want to delete this submission',
			callback: function(val) {
				if (val) {
					console.log('yes: ' + submission_key);

					var data = {
						key: submission_key
					};

					$.post('/_api/forms/delete', data)
					.done(function(result) {
						console.log(result);
						//location.href = location.href;
						vex.dialog.alert({
							message:'Submission deleted. Refreshing page',
							callback: function() {
								window.location = '/admin/forms/';
							}
						});
					})
					.fail(function(result) {
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