function cateChart(labels, data){
    const ctx = document.getElementById('myStatChart');

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: labels,
      datasets: [{
        label: 'So luong',
        data: data,
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}

function revenueChart(labels, data){
    const ctx = document.getElementById('myStatChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'So luong',
        data: data,
        borderWidth: 1,
        backgroundColor: ['red','blue','yellow']
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}