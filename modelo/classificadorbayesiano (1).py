# -*- coding: utf-8 -*-
"""ClassificadorBayesiano.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dYWLaH6t5Md13DW6cUvUw_9hmJXAh2lY
"""

import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.ensemble import RandomForestClassifier

"""**Leitura do conjunto de dados**"""

df_music = pd.read_excel("http://robsonfernandes.net/cci/dataset_genero_musical.xlsx")

df_music.head(5)

len(df_music)

print(df_music["musica"].values[0])

"""##Análise de grupos musicais"""

Counter(df_music["genero"])

"""##Baixar corpos amostral"""

nltk.download("stopwords")

list_stop_words = stopwords.words("portuguese")
print(list_stop_words)

"""##Etapa de limpeza (clean)

"""

#Remover os \n que vem no texto de música responsável por quebrar a linha
#Localiza toda as palavras com \n e substitui ele por vazio. Utiliza regex e já atualiza autmaticamente o proprio dataframe
df_music["musica"].replace('\n', ' ', regex=True, inplace=True);

#Texto limpo sem o \n
df_music["musica"].values[0]

"""##Transformação

"""

#Os modelos mais sofisticados costumam diferenciar letras maiusculas de minuscular, ou seja, nesse caso (Amar !== amar).
#Porem em nosso projeto não faremos essa verificação, para solucionar vamos dar um lower case para nosso texto.
df_music["musica"] = df_music["musica"].str.lower()

df_music["musica"].values[0]

#Garantir que as amostras não possuem NA (Not a number)
df_music = df_music.dropna(axis=0)

#instancia da classe countVectorizer onde como parametro faremos ele ignorar as stopwords
#ngram_range definiremos se vamos consultar unigrama, bigrama (2,2) ou trigrama (3,3)
counter = CountVectorizer(stop_words=list_stop_words, ngram_range= (1, 1))

#Amostra de texto utilizando a primeira musica como exemplo
texto = df_music["musica"].values[0]

#Transformar essa amostra em um vetor
texto_transformado = counter.fit_transform([texto]);

texto_transformado.toarray()

colums = counter.get_feature_names_out()

df_music_tranformado = pd.DataFrame(texto_transformado.toarray(), columns= colums)

df_music_tranformado

"""##Separação amostral em treinamento e teste
- hold-out (tream test split)
    - 70/30
    - 70% das músicas nós treinamos o modelo
    - 30% das músicas nós avaliamos a acertividade do modelo
"""

#x -> features (as letras das musicas) df_music["musica"]
#y -> Amostras (alvo, ou seja o genero)
X = df_music["musica"];
y = df_music["genero"];

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42)

"""##Pipeline para a criação do modelo inferencial"""

model_classify = Pipeline(
    [
        ('Vect', CountVectorizer(stop_words=list_stop_words)), #Primeira etapa -> Pega o texto e transforma em vetor tirando as stopwords
        #('clf', MultinomialNB()), #Chamar o classificador,
        ('clf', RandomForestClassifier(n_estimators=1000)),
    ]
)

#Treinar o modelo
model_classify.fit(X_train.values, y_train.values)

"""#Avaliação do modelo

"""

from sklearn import metrics
#Avaliação geral
model_classify.score(X_test, y_test)

#Realizar a prdição das letras
genero_preds = model_classify.predict(X_test)

print(metrics.classification_report(y_test, genero_preds))

"""##Predição individual"""

letra_individual = '''
Eu sei que vou te amar
Por toda a minha vida eu vou te amar
Em cada despedida eu vou te amar
Desesperadamente eu sei que vou te amar

E cada verso meu será
Pra te dizer
Que eu sei que vou te amar
Por toda minha vida

Eu sei que vou chorar
A cada ausência tua eu vou chorar
Mas cada volta tua há de apagar
O que esta ausência tua me causou

Eu sei que vou sofrer
A eterna desventura de viver
A espera de viver ao lado teu
Por toda a minha vida

Eu sei que vou sofrer
A eterna desventura de viver
A espera de viver ao lado teu
Por toda a minha vida
'''

model_classify.predict([letra_individual])

"""##Salvando a ia em arquivo binario - lib

"""

!pip install joblib

import joblib
model_file = 'music_geral.alisson'
joblib.dump(model_classify, model_file)

"""##como Usar um produção"""

model_ia = joblib.load(model_file)
model_ia.predict([letra_individual])

"""##Avaliar nivel de confiança do modelo

"""

#Qual a porcentagem que ele encontrou para dizer que o genero é sertanejo?
##As opções que ele possui
model_ia.classes_

confianca = model_ia.predict_proba([letra_individual])
confianca

import numpy as np
[np.round(i) for i in confianca]

"""##Instalar line - Modelo explicavel"""

!pip install lime

nome_das_classes = model_ia.classes_
nome_das_classes

#Importando LIME
from lime.lime_text import LimeTextExplainer

#Instanciando o objeto do limeText
explainer_ai = LimeTextExplainer(class_names=nome_das_classes)

#Explicabilidade sendo finalmente aplicada
exp = explainer_ai.explain_instance(letra_individual, model_ia.predict_proba, num_features=5, top_labels=2)

exp.show_in_notebook()