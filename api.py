import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def homepage():
    return 'The API is running...'

@app.route('/api')
def api_return():
    result = pd.read_csv('resultados.csv')
    total = result['Resultado'][0]
    resposta = {f'Resultado {0}': total}
    return jsonify(resposta)


app.run(host = '0.0.0.0')