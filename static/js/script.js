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
	if (Math.max(...context.chart.data.datasets[1].data) <= 5) return 5;
	if (Math.max(...context.chart.data.datasets[1].data) <= 10) return 10;
	if (Math.max(...context.chart.data.datasets[1].data) <= 20) return 20;
	else return 50;
}

function determineTempColor(context) {
	const {ctx, chartArea} = context.chart;
	if (!chartArea) return;
	return getGradient(ctx, chartArea);
}

// This function adds 0's (or another value) to the end of the array until it has a certain length
function addPadding(arr, len, value) {
	return arr.concat(Array(len - arr.length).fill(value))
}


let temp_data = {
	type: 'line',
	label: "Temperature",
	yAxisID: "temp",
	backgroundColor: function(context) {
        const {ctx, chartArea} = context.chart;
		if (!chartArea) return;
        return getGradient(ctx, chartArea);
    },
	borderColor: function(context) {
        const {ctx, chartArea} = context.chart;
		if (!chartArea) return;
        return getGradient(ctx, chartArea);
    },
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

let daily_chart_options = {
	scales: {
		x: {
			grid: {
				tickLength: 0
			},
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
				callback: function(value, index, values) {
					// Hide every odd label and the first and last labels
					return (index % 2 === 1 || index === 0 || index === values.length - 1) ? '' : value;
				}
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
	responsive: true,
};


function initialize() {
	let dailyChart = new Chart('dailyChart', {
		type: 'bar',
		data:  {
			labels: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
			datasets: [temp_data, rain_data]
		},
		options: daily_chart_options
	});

	let map = leaflet("map",{
		Location: [52.1326,5.2913],
		zoom:5
	});
	
	connect_block(dailyChart, 'dailyChart');
	connect_block(map, "map");
}

