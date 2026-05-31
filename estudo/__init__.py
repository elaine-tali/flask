from flask import Flask #importa a biblioteca flask

app = Flask(__name__) #nome do aplicativo sera o mesmo do nome do arquivo //

from estudo.views import homepage