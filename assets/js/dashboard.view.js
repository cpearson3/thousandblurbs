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
	$scope.noSubmissions = false;
	
	$scope.myChartObject = {
		type: 'ColumnChart'
	};
	
	$.get('/_api/forms/')
	.done(function(result) {
		console.log(result);
		
		if (result.length > 0) {
			$scope.submissions = result;
			
			$('#chart-container').show();
			
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
			
			// set up row data array
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
			
			// set up chart
			$scope.myChartObject.data = {
				"cols": [
				    {id: "t", label: "Namespace ID", type: "string"},
				    {id: "s", label: "Submissions", type: "number"}
				],
				"rows": rowData
			};
		
		} else {
			$('#no-chart-data').show();
		}
		
	})
	.fail(function(result){
		console.log('Dashboard Error: Could not retrieve form submissions');
	});
	
}