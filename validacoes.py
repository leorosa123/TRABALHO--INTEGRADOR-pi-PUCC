from flask import Flask, render_template, request, redirect,  url_for
from flask_mysqldb import MySQL
import json

def validacaoLogin(email, senha, banco:"MySQL"):
    if email in banco and senha == banco.login.email.senha:
        return 1
    return 0

def validaCPF(CPF:"str", founder):
    if CPF in founder:
        return 1
    return 0

def validaEmailCadastrado(email:"str", cpf:"str", banco:"MySQL"):
    if email in banco.email or cpf in banco.cpf:
        return 1
    return 0