import pandas as pd
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def homepage():
    return 'The API is running...'

@app.route('/api', methods = ['GET'])
def api_return():
    result = pd.read_csv('resultados.csv')
    index = request.args.get('page', default = 0, type = int)
    total = result['Resultado'][index]
    resposta = {f'Resultado {index}': total}
    return jsonify(resposta)

@app.route('/db', methods = ['GET'])
def db_return():
    conn = sqlite3.connect('api_db.db').cursor()
    index = request.args.get('page', default = 0, type = int)
    for row in conn.execute(f'SELECT * FROM ESPECIME WHERE ID = {index}'):
        query = row[1]
    resposta = {f'Resultado {index}': query}
    return jsonify(resposta)


app.run(host = '0.0.0.0')