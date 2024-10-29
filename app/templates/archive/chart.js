const ctx = document.getElementById('expenseChart').getContext('2d');

// Sample data for each month
const monthlyData = {
    January: {
        spent: [400, 600, 300, 500, 400, 600, 200],
        spendUpTo: [800, 1000, 600, 900, 700, 900, 300]
    },
    February: {
        spent: [500, 700, 350, 600, 450, 700, 250],
        spendUpTo: [850, 1050, 650, 950, 750, 950, 350]
    },
    March: {
        spent: [420, 620, 320, 520, 420, 620, 220],
        spendUpTo: [820, 1020, 620, 920, 720, 920, 320]
    },
    April: {
        spent: [450, 650, 330, 530, 430, 630, 230],
        spendUpTo: [850, 1050, 630, 930, 730, 930, 330]
    },
    May: {
        spent: [480, 680, 340, 540, 440, 660, 240],
        spendUpTo: [880, 1080, 640, 940, 740, 940, 340]
    },
    June: {
        spent: [500, 700, 350, 600, 450, 700, 250],
        spendUpTo: [900, 1100, 650, 1000, 800, 1000, 350]
    },
    July: {
        spent: [520, 740, 370, 620, 470, 720, 260],
        spendUpTo: [920, 1140, 670, 1020, 820, 1020, 370]
    },
    August: {
        spent: [540, 760, 390, 640, 490, 740, 280],
        spendUpTo: [940, 1160, 690, 1040, 840, 1040, 390]
    },
    September: {
        spent: [560, 780, 400, 660, 500, 760, 290],
        spendUpTo: [960, 1180, 700, 1060, 860, 1060, 400]
    },
    October: {
        spent: [580, 800, 420, 680, 520, 780, 300],
        spendUpTo: [980, 1200, 720, 1080, 880, 1080, 420]
    },
    November: {
        spent: [600, 820, 440, 700, 540, 800, 310],
        spendUpTo: [1000, 1220, 740, 1100, 900, 1100, 440]
    },
    December: {
        spent: [640, 840, 430, 690, 580, 770, 340],
        spendUpTo: [1000, 1200, 740, 1100, 880, 1100, 440]
    }
};

// Initial chart data (for January by default)
let currentData = monthlyData.January;

// Chart configuration
const config = {
    type: 'bar',
    data: {
        labels: ['Grocery', 'Rental', 'Regular expense', 'Education', 'Miscellaneous', 'Medical', 'Donation'],
        datasets: [
            {
                label: 'Spent',
                data: currentData.spent,
                backgroundColor: 'rgba(75, 0, 130, 0.8)',
                borderColor: 'rgba(75, 0, 130, 1)',
                borderWidth: 1
            },
            {
                label: 'Spend up to',
                data: currentData.spendUpTo,
                backgroundColor: 'rgba(153, 102, 255, 0.5)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                position: 'top',
            },
        },
    }
};

// Create the chart
let expenseChart = new Chart(ctx, config);

// Function to update the chart data
function updateChart(month) {
    // Get the new data for the selected month
    currentData = monthlyData[month];

    // Update chart datasets with the new data
    expenseChart.data.datasets[0].data = currentData.spent;
    expenseChart.data.datasets[1].data = currentData.spendUpTo;

    // Update the chart display
    expenseChart.update();
}

// Apply button functionality to update the chart when a new month is selected
document.getElementById('apply-btn').addEventListener('click', () => {
    const selectedMonth = document.getElementById('month').value;
    updateChart(selectedMonth);
});
