from flask import Flask, render_template, request, redirect,  url_for
from flask_mysqldb import MySQL
import json

app = Flask(__name__) # Creating flask app
app.config['JSON_SORT_KEYS'] = False

# DB Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'BancoDeDadosHOPE'

mySql = MySQL(app) # SQL Connection

cursor = mySql.connection.cursor() # Cursor do SQL --> usados to execute 

# Base de redirecionamento dentro das paginas
@app.route('/')
def index():
    return render_template('index.html')
# CRUD de informacoes dos usuarios
# Tomada de customizacoes dentro do site para menu e afins
# Validacao do login e informacoes
# Tomada dos horarios e psicologos disponiveis dentro do banco
# CRUD agendamento
# Tomada de realizacao dentro do banco de dados
# Tomada de seguranca dentro da pagina