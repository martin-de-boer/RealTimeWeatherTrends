let temp_chart_options = {
	scales: {
		xAxis: [{
			display: true,
			ticks: {
				beginAtZero: true,
				min:0,
				max: 23
			}
		}],
		yAxis: [{
			display: true,
			ticks: {
				beginAtZero: true,
				min: 0,
				max: 50
			}
		}]
	},
	responsive: true,
};

let temp_data = {
	labels: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
	datasets: [{
		label: "Temperature ",
		backgroundColor: 'rgba(255, 99, 132, 1)',
		borderColor: 'rgba(255, 99, 132, 1)',
		borderWidth: 1,
		data: [20,21,22,22,22,21,19,19,20,18,15]
	}]
};

let rain_data = {
	labels: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
	datasets: [{
		label: 'Rain',
		backgroundColor: 'rgba(3, 120, 158, 0.2)',
		borderColor: 'rgba(3, 120, 158, 1)',
		borderWidth: 1,
		data: [12, 19, 3, 5, 2, 3]
	}]
};


   let tempChart = linechart('tempChart', {
	data: temp_data,
	options: temp_chart_options
});

connect_block(tempChart, 'tempchart_data');

let rainChart = new Chart('rainChart', {
	type: 'bar',
	data: rain_data,
	options: temp_chart_options
});

connect_block(rainChart, 'rainchart_data');

