# Classificação de Gêneros Musicais com NLP e Aprendizado de Máquina

Este projeto consiste em uma aplicação completa que utiliza aprendizado de máquina para classificar gêneros musicais com base nas letras das músicas. A solução é composta por:

- **Back-end**: Desenvolvido em FastAPI, integrando um modelo de aprendizado de máquina treinado.
- **Front-end**: Interface amigável para interação com o modelo preditivo.
- **Modelo de IA**: Um pipeline de NLP para análise e predição baseado em letras musicais.

---

## 🚀 Funcionalidades

- Enviar letras de músicas para análise.
- Receber predições do gênero musical e o nível de confiança da classificação.
- Visualizar os resultados de forma gráfica no front-end.

---

## 🛠️ Instalação

Certifique-se de ter o Python instalado. Execute os seguintes comandos para instalar as dependências:

```bash
pip install fastapi
pip install joblib
pip install uvicorn
pip install scikit-learn
```

Após isso, gere o modelo de aprendizado de máquina no diretório `/modelo`. Consulte o `README.md` dentro desse diretório para mais informações.

---

## 📂 Estrutura do Projeto

```plaintext
/
├── app/
│   ├── main_standalone.py  # Arquivo principal para rodar o back-end
├── front-end/
│   ├── mvc/
│       ├── index.html      # Arquivo de interface gráfica
├── modelo/
│   ├── ...                 # Arquivos relacionados ao modelo treinado
└── README.md               # Documentação do projeto
```

---

## 💻 Como Rodar o Projeto

1. **Inicie o Back-end**:
   
   ```bash
   cd ./app
   python ./main_standalone.py
   ```

2. **Abra o Front-end**:
   
   - Abra o arquivo `front-end/mvc/index.html` no navegador para acessar a interface gráfica.

---

## 📊 Descrição Técnica

### Arquitetura do Sistema

1. **Frontend (Interface do Usuário)**
   - Permite ao usuário inserir letras de músicas.
   - Exibe os resultados da predição e um gráfico de confiança.
   - Comunicação com o back-end via API.

2. **Backend (FastAPI)**
   - Recebe as requisições do front-end.
   - Carrega o modelo de aprendizado de máquina.
   - Realiza as predições e retorna a resposta em JSON.

3. **Modelo de IA (Arquivo .joblib)**
   - Armazena o classificador treinado.
   - Realiza as predições com base no texto recebido.

### Componentes

#### Diagrama de Caso de Uso

- **Atores**:
  - **Usuário**: Insere letras e visualiza os resultados.
  - **Servidor**: Processa os textos e retorna as predições.
- **Casos de Uso**:
  - Enviar letra de música.
  - Receber predições e nível de confiança.

#### Diagrama de Sequência

1. O usuário insere a letra de uma música e clica no botão de predição.
2. O front-end realiza uma requisição HTTP POST para o endpoint FastAPI.
3. O back-end processa os dados, realiza a predição e retorna o resultado.
4. O front-end exibe a predição e os níveis de confiança ao usuário.

#### Diagrama de Classes

- **FastAPI**: Gerencia os endpoints.
- **BaseModel**: Define o esquema de entrada (letra da música).
- **ModeloCarregado**: Representa o modelo treinado e realiza as predições.
- **Pipeline**: Inclui o `CountVectorizer` e o classificador.

---

## 🎯 Objetivo do Projeto

Demonstrar como técnicas de **Processamento de Linguagem Natural (NLP)** e **Aprendizado de Máquina** podem ser aplicadas para:

- Classificar automaticamente textos em domínios específicos (neste caso, músicas).
- Fornecer uma solução acessível e automatizada para a análise musical.

### Pipeline do Modelo

1. Pré-processamento das letras:
   - Remoção de stopwords.
   - Normalização dos textos.
2. Vetorização com `CountVectorizer`.
3. Treinamento com o classificador `Random Forest`.
4. Salvamento do modelo treinado para uso em produção.

---

## 🌐 Tecnologias Utilizadas

- **Back-end**: FastAPI, Python.
- **Front-end**: HTML, CSS, JavaScript.
- **Machine Learning**: Scikit-learn, Joblib.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para a sua funcionalidade.
3. Faça commit das suas alterações.
4. Abra um Pull Request.

---

