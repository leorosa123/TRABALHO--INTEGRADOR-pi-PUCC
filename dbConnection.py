from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__) # Creating flask app
app.config['JSON_SORT_KEYS'] = False

# DB Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'BancoDeDadosHOPE'

# Pointing to db
mySql = MySQL(app) # SQL Connection