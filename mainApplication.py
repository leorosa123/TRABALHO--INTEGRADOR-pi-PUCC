# Structural import
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from dbConnection import mySql

app = Flask(__name__)

# Rota para renderizar o formulário
@app.route('/')
def index():
    return render_template('../front-end/view/index.html')

# POST for js
@app.route('/api/dados', methods=['POST'])
def enviar_dados():
    # Pegando as informacoes dentro do json
    return jsonify()


if __name__ == '__main__':
    app.run(debug=True)