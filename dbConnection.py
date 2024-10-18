from flask import Flask
import flask_mysqldb as db

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "<p>Hello!!</p>"

# DB Connection
# CRUD de informacoes dos usuarios
# Tomada de customizacoes dentro do site para menu e afins
# Validacao do login e informacoes
# Tomada dos horarios e psicologos disponiveis dentro do banco
# CRUD agendamento
# Tomada de realizacao dentro do banco de dados
# Tomada de seguranca dentro da pagina