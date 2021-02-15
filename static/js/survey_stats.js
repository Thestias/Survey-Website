window.onload = function () {

    function create_chart(question, list_labels, list_data) {
        var chart_creation = document.createElement('canvas')
        chart_creation.classList.add('chart')
        var separator = document.createElement('hr')
        separator.classList.add('mt-8', 'mb-12')
        document.querySelector('#charts-wrapper').insertAdjacentElement('beforeend', chart_creation)
        document.querySelector('#charts-wrapper').insertAdjacentElement('beforeend', separator)

        var chart = new Chart(chart_creation.getContext('2d'), {
            // The type of chart we want to create
            type: 'doughnut',

            // The data for our dataset
            data: {
                labels: list_labels, // OPTIONS //////////////////////////////
                datasets: [{
                    data: list_data, // ANSWERS //////////////////////////////
                    backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)'
                    ],
                    borderColor: '#fff',
                    borderWidth: 3
                }]
            },

            // Configuration options go here
            options: {
                responsive: true,
                legend: {
                    position: 'bottom',
                },
                animation: {
                    animateScale: true,
                    animateRotate: true
                },
                title: {
                    display: true,
                    text: 'Question: ' + question // QUESTION //////////////////////////////////7
                }
            }
        });
    }

    let survey_data = document.querySelector('#submission_data').firstChild.data
    if (survey_data != 'null') {
        survey_data = JSON.parse(survey_data)
        for (const [key, value] of Object.entries(survey_data)) {
            create_chart(key, value[0], value[1]);
            console.log(value[0], value[1])
        }
    }
}