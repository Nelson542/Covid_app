document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('confirmed', {
        chart: {
            type: 'line',
            backgroundColor: '#222',
            height: 275,
            width:400,
        },
        title: {
            text: 'Confirmed',
            style: {
                color: '#d90537'
              }
        },
        xAxis: {
            type: 'datetime',
            labels: {
                style: {
                  color: '#efefef'
                }
              },        
            categories: dates.map(date => {
            return Highcharts.dateFormat('%d-%b', new Date(date).getTime());
          })
                
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
            color: '#d90537'
        }, ],

        navigation: {buttonOptions: {enabled: false}},
        legend:{ enabled:false },
        credits: {enabled: false}
    });
});



document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('active', {
        chart: {
            type: 'line',
            backgroundColor: '#222',
            height: 275,
            width:400
        },
        title: {
            text: 'Active',
            style: {
                color: '#5355f6'
              }
        },
        xAxis: {
            type: 'datetime',
            labels: {
                style: {
                  color: '#efefef'
                }
              },        
            categories: dates.map(date => {
            return Highcharts.dateFormat('%d-%b', new Date(date).getTime());
          })
                
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
            name: 'Active',
            data: active_count,
            color: '#5355f6'
        }, ],

        navigation: {buttonOptions: {enabled: false}},
        legend:{ enabled:false },
        credits: {enabled: false}
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('recovered', {
        chart: {
            type: 'line',
            backgroundColor: '#222',
            height: 275,
            width:400
        },
        title: {
            text: 'Recovered',
            style: {
                color: '#0db111'
              }
        },
        xAxis: {
            type: 'datetime',
            labels: {
                style: {
                  color: '#efefef'
                }
              },        
            categories: dates.map(date => {
            return Highcharts.dateFormat('%d-%b', new Date(date).getTime());
          })
                
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
            name: 'Recovered',
            data: recovered_count,
            color: '#0db111'
        }, ],

        navigation: {buttonOptions: {enabled: false}},
        legend:{ enabled:false },
        credits: {enabled: false}
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('deceased', {
        chart: {
            type: 'line',
            backgroundColor: '#222',
            height: 275,
            width:400
        },
        title: {
            text: 'Deceased',
            style: {
                color: '#a0a8a2'
              }
        },
        xAxis: {
            type: 'datetime',
            labels: {
                style: {
                  color: '#efefef'
                }
              },        
            categories: dates.map(date => {
            return Highcharts.dateFormat('%d-%b', new Date(date).getTime());
          })
                
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
            name: 'Deceased',
            data: deceased_count,
            color: '#a0a8a2'
        }, ],

        navigation: {buttonOptions: {enabled: false}},
        legend:{ enabled:false },
        credits: {enabled: false}
    });
});




document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('infection', {
        chart: {
            type: 'bar',
            backgroundColor: '#222',
            height: 600,
            width:700
        },
        title: {
            text: ''
        },
        xAxis: {
            type: 'datetime',
            labels: {
                style: {
                  color: '#efefef'
                }
              },        
            categories: dates.map(date => {
            return Highcharts.dateFormat('%d-%b', new Date(date).getTime());
          })
                
          },
        yAxis: {
            min: 0,
            title: {
                text: 'No of people',
                align: 'high',
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
        tooltip: {
            valueSuffix: ' people'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 80,
            floating: true,
            borderWidth: 1,
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || '#e6dcdc',
            shadow: true
           
        },
        
        series: [{
            name: 'Confirmed',
            data: confirmed_count,
            color: '#d90537'
        }, {
            name: 'Active',
            data: active_count,
            color: '#5355f6'
        }, {
            name: 'Recovered',
            data: recovered_count,
            color: '#0db111'
        }, {
            name: 'Deceased',
            data: deceased_count,
            color: '#a0a8a2'
        }],
        navigation: {buttonOptions: {enabled: false}},
        credits: {enabled: false},
        
    });
});
