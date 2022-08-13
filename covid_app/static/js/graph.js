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


document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('testing', {
        chart: {
            type: 'column',
            backgroundColor: '#222',
            height: 550,
            width:600
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
      
        
        series: [{
            name: 'Positive',
            data: confirmed_count,
            color: '#d90537'
        }, {
            name: 'Negative',
            data: negative_results,
            color: '#5355f6'
        }],
        navigation: {buttonOptions: {enabled: false}},
        credits: {enabled: false},
        legend:{ itemStyle: {
            color: '#A0A0A0'
         },
         itemHoverStyle: {
            color: '#FFF'
         },
         itemHiddenStyle: {
            color: '#444'
         } },
        
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('age_graph', {
        chart: {
            type: 'pie',
            backgroundColor: '#222',
            height: 400,
            width:600,
        },
        title: {
            text: 'Age-wise Summary',
            style: {
                color: '#efefef'
              }

        },
        tooltip: {
            pointFormat: '<b>{point.y} people</b>',
            
        },
        accessibility: {
            point: {
                valueSuffix: '%'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: '#efefef'
                      }

                },
                borderColor:'#222'
            }
        },
        series: [{
            name: 'Age',
            colorByPoint: true,
            data: [{
                name: '0 - 18 Years',
                y: age1,
                sliced: true,
                selected: true,
                color: '#c03f45'
            }, {
                name: '19 - 40 Years',
                y: age2,
                color: '#3992a9'
            },  {
                name: '41 - 60 Years',
                y: age3,
                color: '#bbb947'
            }, {
                name: 'Above 60 Years',
                y: age4,
                color: '#33873e'

            }]

           
            
        }],
        navigation: {buttonOptions: {enabled: false}},
        credits: {enabled: false},
        legend:{ itemStyle: {
            color: '#A0A0A0'
         },
         itemHoverStyle: {
            color: '#FFF'
         },
         itemHiddenStyle: {
            color: '#444'
         } },

    });
});
