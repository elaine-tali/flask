from estudo import app
from flask import render_template, url_for

@app.route('/') #é a rota apos a barra no navegador

def homepage(): #é uma função para retornar 
    return render_template('index.html')

@app.route('/nova/') 

def novapage():  
    return 'outra view'