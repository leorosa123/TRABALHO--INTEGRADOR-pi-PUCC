from flask import Flask, render_template, request 
from flask_mysqldb import MySQL
import json

app = Flask(__name__) # Creating flask app

# DB Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'BancoDeDadosHOPE'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mySql = MySQL(app) # SQL Connection

cursor = mySql.connection.cursor() # Cursor do SQL --> usados to execute 

# CRUD de informacoes dos usuarios
# Tomada de customizacoes dentro do site para menu e afins
# Validacao do login e informacoes
# Tomada dos horarios e psicologos disponiveis dentro do banco
# CRUD agendamento
# Tomada de realizacao dentro do banco de dados
# Tomada de seguranca dentro da pagina