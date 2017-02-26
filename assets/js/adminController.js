/* Admin controller */

/* global $ */
/* global angular */
/* global location */
/* global vex */

export function AdminController($scope, $timeout) {
	console.log('in the dashboard');

	$scope.delete = function(submission_key) {
		vex.dialog.confirm({
			message: 'Are you sure you want to delete this contact',
			callback: function(val) {
				if (val) {
					console.log('yes: ' + submission_key);

					var data = {
						key: submission_key
					};

					$.post('/_api/v1/delete/', data)
					.done(function(result) {
						console.log(result);
						//location.href = location.href;
						vex.dialog.alert({
							message:'Contact deleted. Refreshing page',
							callback: function() {
								$timeout(function() {
									location.reload(true);
								}, 300)
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