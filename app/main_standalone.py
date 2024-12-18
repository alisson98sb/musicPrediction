from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel #Criação de metadados - Informações de um dado, o tipo dele, tamanho... 
import joblib
import uvicorn

# Inicializar o app FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #ou allow_origins=["www.google.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar o modelo com joblib
modelo = joblib.load('models/music_geral.alisson')

# Modelo de dados para receber o texto
class TextoEntrada(BaseModel): #extends basemodel, ou seja textoEntrada esta herdando basemodel
    texto: str

@app.post("/api/v1/ai/music/prediction")
async def realizar_predicao(dados: TextoEntrada):
    try:
        # Realizar a predição e obter a confiança
        predicao = modelo.predict([dados.texto])[0]
        confianca = modelo.predict_proba([dados.texto])[0]

        # Construir a resposta JSON com predição e confiança
        resposta = {
            "predicao": predicao,
            "confianca": {
                classe: round(prob * 100, 2)  # Converte para porcentagem com 2 casas decimais
                for classe, prob in zip(modelo.classes_, confianca)
            }
        }
        return resposta
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Código para rodar o servidor com uvicorn diretamente no script
if __name__ == "__main__":
    uvicorn.run("main_standalone:app", host="0.0.0.0", port=8000, reload=True)