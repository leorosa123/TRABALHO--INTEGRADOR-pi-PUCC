# Structural import
from flask import Flask, render_template, request, redirect,  url_for
from flask_mysqldb import MySQL
import json

# Importing packeges and necessary functions
from client import loggedClient
import validacoes
from dbConnection import app

mySql = MySQL(app) # SQL Connection

cursor = mySql.connection.cursor()