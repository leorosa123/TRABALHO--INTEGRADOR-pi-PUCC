# Structural import
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from dbConnection import mySql

app = Flask(__name__)

# Rota para renderizar o formulário
@app.route('/')
def index():
    return render_template('../front-end/view/index.html')

# Rota para receber dados via POST do JavaScript
@app.route('/enviar', methods=['POST'])
def enviar_dados():
    # Pegando as informacoes dentro do json
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    # Jogando as informacoes dentro do banco de dados

    return jsonify({'message': 'Dados salvos com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)