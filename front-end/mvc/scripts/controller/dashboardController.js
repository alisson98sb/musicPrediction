import { DashboardModel } from '../model/dashboardModel.js';
import { DashboardView } from '../view/dashboardView.js';

const handlePrediction = async () => {
  const texto = DashboardView.getInputText();

  if (!texto) {
    DashboardView.displayResult("Por favor, insira um texto.");
    return;
  }

  try {
    const prediction = await DashboardModel.makePrediction(texto);
    DashboardView.displayResult(`Predição: ${prediction.predicao}`);
    
    // Usa diretamente o objeto `confianca` para gerar o gráfico
    if (prediction.confianca && typeof prediction.confianca === 'object') {
      DashboardView.renderChart(prediction.confianca);
    } else {
      throw new Error("Formato de dados inválido: 'confianca' não é um objeto.");
    }
  } catch (error) {
    DashboardView.displayResult(`Erro: ${error.message}`);
  }
};
// Inicializar o controlador
DashboardView.bindPredictButton(handlePrediction);