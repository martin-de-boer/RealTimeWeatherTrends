temp_gradient = [
	"#2B3789",
	"#314491",
	"#4D65AB",
	"#5975B6",
	"#6582BE",
	"#748EC7",

	"#829ED0",
	"#93ABD9",
	"#A2B8E1",
	"#A6C2D8",

	

	// Yellow
	"#D8DD83",
	"#E5D975",
	"#ECD76A",
	"#EFCB59",
	"#E6B33E",

	"#DD9A25",
	"#DC9322",
	"#DA8324",
	"#D4741E",
	"#D16524",

	// Reds, oranges
	"#CC5626",
	"#CA4C23",
	"#CA4C23",
	"#BA371B",
	"#B32A17",
	"#A70F0E",
	"#9B1015"

]

const CHART_COLORS = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)'
  };

let width, height, gradient;
function getGradient(ctx, chartArea) {
  const chartWidth = chartArea.right - chartArea.left;
  const chartHeight = chartArea.bottom - chartArea.top;
  if (!gradient || width !== chartWidth || height !== chartHeight) {
    // Create the gradient because this is either the first render
    // or the size of the chart has changed
    width = chartWidth;
    height = chartHeight;
    gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
    gradient.addColorStop(0, CHART_COLORS.blue);
    gradient.addColorStop(0.5, CHART_COLORS.yellow);
    gradient.addColorStop(1, CHART_COLORS.red);
  }

  return gradient;
}

function determineMaxRain(context) {
	// if (Math.max(...context.chart.data.datasets[1].data) <= 4) return 5;
	// if (Math.max(...context.chart.data.datasets[1].data) <= 9) return 10;
	// if (Math.max(...context.chart.data.datasets[1].data) <= 20) return 20;
	// else return 50;
	return 50;
}

function determineTempColor(context) {
	const {ctx, chartArea} = context.chart;
	if (!chartArea) return;
	return getGradient(ctx, chartArea);
}

function determineLabelDisplay(value, index, values) {
	if (index % 2 === 1 || index === 0 || index === values.length - 1) 
		return '';
	else 
		return value;
}


let temp_data = {
	type: 'line',
	label: "Temperature",
	yAxisID: "temp",
	backgroundColor: (context) => determineTempColor(context),
	borderColor: (context) => determineTempColor(context),
	borderWidth: 1,
	data: []
};

let rain_data = {
	label: 'Rain',
	yAxisID: "rain",
	backgroundColor: 'rgba(3, 120, 158, 0.2)',
	borderColor: 'rgba(3, 120, 158, 1)',
	borderWidth: 1,
	barPercentage: 1.33,
	data: []
}

let temp_data2 = {
	type: 'line',
	label: "Temperature",
	yAxisID: "temp",
	backgroundColor: (context) => determineTempColor(context),
	borderColor: (context) => determineTempColor(context),
	borderWidth: 1,
	data: []
};

let rain_data2 = {
	label: 'Rain',
	yAxisID: "rain",
	backgroundColor: 'rgba(3, 120, 158, 0.2)',
	borderColor: 'rgba(3, 120, 158, 1)',
	borderWidth: 1,
	barPercentage: 1.33,
	data: []
}

let daily_chart_options = {
	scales: {
		x: {
			grid: { tickLength: 0 },
			display: true,
			ticks: {
				beginAtZero: true,
				min: 0,
				max: 24,
				padding: 0, // display label inside chart,
				mirror: true,
				rotation: 0,
				minRotation: 0,
				maxRotation: 0,
				// Hide every odd label and the first and last labels
				callback: (value, index, values) => determineLabelDisplay(value, index, values)
			}
		},
		temp: {
			position: 'left',
			display: true,
			min: (context) => Math.floor(Math.min(...context.chart.data.datasets[0].data) - 3),
			max: (context) => Math.ceil(Math.max(...context.chart.data.datasets[0].data) + 3),
			ticks: {
				rotation: 0,
				callback: function(value, index, values) {
					// Hide first and last labels
					return (index === 0 || index === values.length - 1) ? '' : value;
				}
			}
		},
		rain: {
			position: 'right',
			display: true,
			min: 0,
			max: (context) => determineMaxRain(context),
			grid: {
				drawOnChartArea: false
			},
			ticks: {
				rotation: 0,
				callback: function(value, index, values) {
					// Hide first and last labels
					return (index === 0 || index === values.length - 1) ? '' : value;
				}
			}
		}
	},
	animation: {
		duration: 0
	},
	responsive: true,
};

let prediction_chart_options = {
	scales: {
		x: {
			grid: { tickLength: 0 },
			display: true,
			ticks: {
				padding: 0, // display label inside chart,
				mirror: true,
				rotation: 0,
				minRotation: 0,
				maxRotation: 0,
			}
		},
		temp: {
			position: 'left',
			display: true,
			min: (context) => Math.floor(Math.min(...context.chart.data.datasets[0].data) - 3),
			max: (context) => Math.ceil(Math.max(...context.chart.data.datasets[0].data) + 3),
			ticks: {
				rotation: 0,
				callback: function(value, index, values) {
					// Hide first and last labels
					return (index === 0 || index === values.length - 1) ? '' : value;
				}
			}
		},
		rain: {
			position: 'right',
			display: true,
			min: 0,
			max: (context) => determineMaxRain(context),
			grid: {
				drawOnChartArea: false
			},
			ticks: {
				rotation: 0,
				callback: function(value, index, values) {
					// Hide first and last labels
					return (index === 0 || index === values.length - 1) ? '' : value;
				}
			}
		}
	},
	animation: {
		duration: 0
	},
	responsive: true,
};

function initialize() {
	document.getElementById("tweets").style.height = 300;	
	let daily_chart = barchart('daily_chart_div', {
		data:  {
			labels: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
			datasets: [temp_data, rain_data]
		},
		options: daily_chart_options
	});

	let map = leaflet("map_div",{
		Location: [52.1326, 5.2913],
		zoom:5
	});

	var prediction_chart = barchart('prediction_chart_div', {
		data: {
			datasets: [temp_data2, rain_data2]
		},
		options: prediction_chart_options
	});

	
	var tweet = tweets("tweets");

	connect_block(daily_chart, 'daily_chart_key');
	connect_block(map, "map_key");
	connect_block(tweet, 'x');
	connect_block(prediction_chart, 'prediction_chart_key');

	var log1 = log_block('log_loc');
    connect_block(log1, 'log_loc_key');

	var log2 = log_block('log_temp');
    connect_block(log2, 'log_temp_key');

	var log3 = log_block('log_rain');
    connect_block(log3, 'log_rain_key');

	var log4 = log_block('log_uv');
    connect_block(log4, 'log_uv_key');

	var log5 = log_block('log_wd');
    connect_block(log5, 'log_wd_key');

	var log6 = log_block('log_wf');
    connect_block(log6, 'log_wf_key');

	var log7 = log_block('log_ws');
    connect_block(log7, 'log_ws_key');

	var log8 = log_block('log_hum');
    connect_block(log8, 'log_hum_key');

	var log9 = log_block('log_ps');
    connect_block(log9, 'log_ps_key');

	var log10 = log_block('log_ps_change');
    connect_block(log10, 'log_ps_change_key');

}

