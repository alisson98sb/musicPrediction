
pip install fastapi
pip install joblib
pip install uvicorn
pip install scikit-learn

Extrair arquivo app/models/music_geral.zip para o app/models/music_geral.alisson

cd ./app 
    python ./main_standalone.py

Com a api rodando, abrir o arquivo front-end/mvc/index.html no navegador. 

O projeto apresentado consiste em uma aplicação completa que utiliza
aprendizado de máquina para realizar a classificação de gêneros musicais
com base em letras de músicas.
A solução foi desenvolvida utilizando o framework FastAPI no back-end,
integrado a um modelo de aprendizado de máquina treinado com dados de
gêneros musicais.
O front-end, por sua vez, proporciona uma interface amigável para interação
com o modelo preditivo. O principal objetivo é demonstrar como técnicas de
processamento de linguagem natural (NLP) e aprendizado de máquina podem
ser aplicadas na classificação automática de textos em um domínio específico,
neste caso, o musical.


• 1. Diagrama de Caso de Uso:
• O sistema possui dois atores principais: o usuário (cliente do front-end) e o
servidor (back-end).
• Usuário: Interage com a interface gráfica para inserir letras de músicas e
visualizar as predições.
• Servidor: Processa os textos enviados, realiza a predição utilizando o
modelo de aprendizado de máquina e retorna os resultados.
• Casos de uso:
• Enviar letra de música.
• Receber a predição e o nível de confiança.

• 2. Diagrama de Sequência
• O usuário insere a letra de uma música e clica no botão de predição.
• O front-end faz uma requisição HTTP POST para o endpoint do FastAPI.
• O back-end carrega o modelo, processa os dados, realiza a predição e
retorna o resultado.
• O front-end exibe a predição e os níveis de confiança ao usuário por meio
de um gráfico.

• 3. Diagrama de Classes
• FastAPI: Classe responsável por gerenciar os endpoints.
• BaseModel: Define o esquema de entrada (letra da música).
• ModeloCarregado: Representa o modelo treinado, responsável pelas
predições.
• Pipeline: Etapa do treinamento que envolve o CountVectorizer e o
classificador escolhido


4. Diagrama de Macro-Arquitetura:
• Frontend (Interface do Usuário)
• O usuário insere a letra da música.
• Visualiza os resultados da predição e o gráfico de
confiança.
• Comunicação com o Backend via API.
• Backend (FastAPI)
• Processa as requisições recebidas do Frontend.
• Carrega o modelo de aprendizado de máquina.
• Realiza as predições e calcula as porcentagens de
confiança.
• Retorna a resposta JSON ao Frontend.
• Modelo de IA (Arquivo serializado .joblib)
• Armazena o classificador treinado.
• Realiza as predições com base no texto recebido.


• A proposta do projeto é fornecer uma solução automatizada e acessível para
classificação de gêneros musicais, utilizando técnicas modernas de
aprendizado de máquina.
• O pipeline do modelo inclui:
- Pré-processamento das letras para remoção de stopwords e normalização.
- Vetorização dos textos com CountVectorizer.
- Treinamento de um modelo de classificação utilizando Random Forest.
- Salvamento do modelo treinado para uso em produção.
O front-end foi projetado para ser simples e intuitivo, permitindo que usuários
não técnicos utilizem a ferramenta para análise musical.

