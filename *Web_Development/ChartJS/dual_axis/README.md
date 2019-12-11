# Chart JS - Dual Axis 

https://stackoverflow.com/questions/38085352/how-to-use-two-y-axes-in-chart-js-v2

```js 
var canvas = document.getElementById('chart');
new Chart(canvas, {
  type: 'line',
  data: {
    labels: ['1', '2', '3', '4', '5'],
    datasets: [{
      label: 'A',
      yAxisID: 'A',
      data: [100, 96, 84, 76, 69]
    }, {
      label: 'B',
      yAxisID: 'B',
      data: [1, 1, 1, 1, 0]
    }]
  },
  options: {
    scales: {
      yAxes: [{
        id: 'A',
        type: 'linear',
        position: 'left',
      }, {
        id: 'B',
        type: 'linear',
        position: 'right',
        ticks: {
          max: 1,
          min: 0
        }
      }]
    }
  }
});
```