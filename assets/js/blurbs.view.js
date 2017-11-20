/* View Blurb controller */

/* global $ */
/* global angular */
/* global location */
/* global vex */

export function ViewBlurbController($scope, $timeout) {
	console.log('viewing blurbs');
	
	$scope.data = {
		metadata: {
			background: $('#blurbBackground').html(),
			themeClass: $('#blurbThemeClass').html()
		},
		content: $('#blurbContent').html(),
		namespaceID: $('#blurbNamespace').html(),
		blurbID: $("#blurbID").html(),
		blurbKey: $('#blurbKey').html()
	};
	
	
	console.log($scope.data);
	
	$scope.delete = function(blurb_key) {
		vex.dialog.confirm({
			message: 'Are you sure you want to delete this blurb?',
			callback: function(val) {
				if (val) {
					console.log('yes: ' + blurb_key);

					var data = {
						key: blurb_key
					};

					$.post('/_api/blurbs/delete', data)
					.done(function(result) {
						console.log(result);
						//location.href = location.href;
						vex.dialog.alert({
							message:'Blurb deleted.',
							callback: function() {
								window.location = '/admin/blurbs/';
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
	
	$scope.save = function(blurb_key) {
		vex.dialog.confirm({
			message: 'Are you sure you want to save blurb?',
			callback: function(val) {
				if (val) {
					console.log('yes: ' + blurb_key);

					var data = {
						key: blurb_key,
						namespaceID: $scope.data.namespaceID,
						blurbID: $scope.data.blurbID,
						metadata: JSON.stringify($scope.data.metadata),
						content: $scope.data.content,
					};
					
					console.log(data);

					$.post('/_api/blurbs/save', data)
					.done(function(result) {
						console.log(result);
						//location.href = location.href;
						vex.dialog.alert({
							message:'Blurb saved.',
							callback: function() {
								window.location = '/admin/blurbs/view?key='+$scope.data.blurbKey;
							}
						});
					})
					.fail(function(result) {
						console.log(result);
						vex.dialog.alert('Could not save');
					});
				} else {
					console.log('i see you do not want to save this.');
				}
			}
		});
	};
}