document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('confirmed', {
        chart: {
            type: 'line',
            backgroundColor: 'rgba(0,0,0,0)'
        },
        title: {
            text: 'Confirmed',
            style: {
                color: '#efefef'
              }
        },
        xAxis: {
            type: 'datetime',
           
            labels: {
            
            style: {
                color: '#efefef'
              },
            },
            categories: dates,
            
        },
        yAxis: {
            title: {
                text: 'No of people',
                style: {
                    color: '#efefef'
                  }
            },
            labels: {
                style: {
                  color: '#efefef'
                }
              },
            gridLineColor: 'transparent',  
            
        },
        series: [{
            name: 'Confirmed',
            data: confirmed_count,
            color: 'tomato'
        }, ],

        navigation: {
            buttonOptions: {
                enabled: false
            }
        },
        legend:{ enabled:false }


    });
});



document.addEventListener('DOMContentLoaded', function () {
    const chart1 = Highcharts.chart('active', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Active'
        },
        xAxis: {
            type: 'datetime',
            labels: {
            format: '{value:%Y-%b-%e}'
            },
            categories: dates
        },
        yAxis: {
            title: {
                text: 'No of people'
            }
        },
        series: [{
            name: 'Active',
            data: active_count
        }, ]
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const chart1 = Highcharts.chart('recovered', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Recovered'
        },
        xAxis: {
            type: 'datetime',
            labels: {
            format: '{value:%Y-%b-%e}'
            },
            categories: dates
        },
        yAxis: {
            title: {
                text: 'No of people'
            }
        },
        series: [{
            name: 'Recovered',
            data: recovered_count
        }, ]
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const chart1 = Highcharts.chart('deceased', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Deceased'
        },
        xAxis: {
            type: 'datetime',
            labels: {
            format: '{value:%Y-%b-%e}'
            },
            categories: dates
        },
        yAxis: {
            title: {
                text: 'No of people'
            }
        },
        series: [{
            name: 'Deceased',
            data: deceased_count
        }, ]
    });
});