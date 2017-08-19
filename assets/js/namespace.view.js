/* View Namespace controller */

/* global $ */
/* global angular */
/* global location */
/* global vex */

export function ViewNamespaceController($scope, $timeout) {
	console.log('viewing namespaces');

	$scope.delete = function(namespace_key) {
		vex.dialog.confirm({
			message: 'Are you sure you want to delete this namespace',
			callback: function(val) {
				if (val) {
					console.log('yes: ' + namespace_key);

					var data = {
						key: namespace_key
					};

					$.post('/_api/namespace/delete', data)
					.done(function(result) {
						console.log(result);
						//location.href = location.href;
						vex.dialog.alert({
							message:'Namespace deleted.',
							callback: function() {
								window.location = '/admin/namespace/';
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