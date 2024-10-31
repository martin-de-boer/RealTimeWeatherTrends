function barchart(id, config = {}) {
    const ctx = document.getElementById(id);
    const chart = new Chart(ctx, {
        type: 'bar',
        data: config.data || {
            labels: [],
            datasets: [{
                label: "Dataset 1",
                data: [],
                backgroundColor: "rgba(255, 99, 132, 0.6)",
                borderWidth: 1
            }]
        },
        options: config.options || {}
    });

    function onEvent(data) {
        // Expecting data in the form {action: "set", value: [category, value, datasetIndex]}
        const [category, value, datasetIndex] = data.value;

        // Ensure the dataset index is valid, creating the dataset if it doesn't exist
        if (!chart.data.datasets[datasetIndex]) {
            chart.data.datasets[datasetIndex] = {
                label: `Dataset ${datasetIndex + 1}`,
                data: new Array(chart.data.labels.length).fill(0), // Initialize with zeros
                backgroundColor: "rgba(54, 162, 235, 0.6)",
                borderWidth: 1
            };
        }

        switch (data.action) {
            case "set":
                // If the category doesn't exist, add it and initialize values for all datasets
                if (!chart.data.labels.includes(category)) {
                    chart.data.labels.push(category);
                    chart.data.datasets.forEach(ds => ds.data.push(0)); // Add zero for each dataset
                }
                
                // Update the value for the specified dataset and category
                const setIndex = chart.data.labels.indexOf(category);
                chart.data.datasets[datasetIndex].data[setIndex] = value;
                break;
            
            case "reset":
                // Clear all labels and data
                chart.data.datasets.forEach(ds => ds.data = []);
                break;
            
            default:
                console.warn("Unsupported action:", data.action);
        }
        
        // Update the chart to apply changes
        chart.update();
    }

    // Return the onEvent function for external calls
    return onEvent;
}