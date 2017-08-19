/* DashboardController */

/* global $ */
/* global angular */
/* global location */
/* global vex */

export function DashboardController($scope) {

	console.log('in the dashboard');
	
	$scope.submissions = [];
	$scope.namespaceIDs = [];
	$scope.formIDs = [];
	$scope.namespaceSubmissions = {};
	
	$scope.myChartObject = {
		type: 'ColumnChart'
	};
	
	$.get('/_api/forms/')
	.done(function(result) {
		console.log(result);
		
		$scope.submissions = result;
		
		for (var i=0;i<result.length;i++) {
			var v_id = result[i]['namespaceID'];
			console.log(v_id)
			
			if ($scope.namespaceIDs.includes(v_id)) {
				// increment counter
				$scope.namespaceSubmissions[v_id] = $scope.namespaceSubmissions[v_id] + 1;
			} else {
				// add to list
				$scope.namespaceIDs.push(v_id);
				$scope.namespaceSubmissions[v_id] = 1;
			}
		}
		
		//console.log($scope.namespaceSubmissions);
		
		var rowData = [];
		
		for (var i in $scope.namespaceSubmissions) {
			var o = $scope.namespaceSubmissions[i];
			rowData.push({
				c: [
					{v: i},
					{v: o}
				]
			});
		}
		
		// set up graph
		
		$scope.myChartObject.data = {
			"cols": [
			    {id: "t", label: "Namespace ID", type: "string"},
			    {id: "s", label: "Submissions", type: "number"}
			],
			"rows": rowData
		};
		
	})
	.fail(function(result){
		console.log('Dashboard Error: Could not retrieve form submissions');
	});
	
}