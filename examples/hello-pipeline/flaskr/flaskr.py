from flask import Flask, request
from werkzeug import Response
import numpy as np
import pandas as pd
import pickle

import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def to_df(raw_data):
    df = pd.DataFrame(data=raw_data)
    return df

def numbers_to_species(number):
    conversion_json = {
        "Iris-setosa": 0,
        "Iris-virginica": 1,
        "Iris-versicolor": 2
    }

    for key, value in conversion_json.items():
        number = number.replace(str(value), key)

    return number

@app.before_first_request
def load_model():
    global model

    app.logger.info('carregando o modelo')

    with open('./assets/pickled.pkl', 'rb') as file:
        model = pickle.load(file)

    app.logger.info('modelo carregado com sucesso')

@app.route('/')
def health():
    return Response('Healthy!', status=200)

@app.route('/predict')
def predict():
    global model

    raw = request.json
    df = to_df(raw)
    prediction = model.predict(df)

    return Response(numbers_to_species(np.array_str(prediction)), status=200)
