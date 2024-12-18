export const DashboardView = {
    getInputText() {
      return document.querySelector('#input-text').value.trim();
    },
    displayResult(message) {
      const resultDiv = document.querySelector('#result');
      resultDiv.textContent = message;
    },
    bindPredictButton(handler) {
      const predictButton = document.querySelector('#predict-btn');
      predictButton.addEventListener('click', handler);
    },
    renderChart(data) {
      const ctx = document.getElementById('confidence-chart').getContext('2d');
      
      // Se um gráfico já existe, destrua-o antes de criar outro
      if (this.chart) {
        this.chart.destroy();
      }
      
      // Crie o novo gráfico
      this.chart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: Object.keys(data),
          datasets: [
            {
              label: 'Confiança (%)',
              data: Object.values(data),
              backgroundColor: [
                '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0',
              ],
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'bottom',
            },
          },
        },
      });
    },
};