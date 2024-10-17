from flask import Flask, render_template# desde la clase flask esta importando el paquete de flask
import mysql.connector
from mysql.connector import Error
from flask_login import login_manager

from My_Garden import models, routes

app = Flask(__name__) #crea una instancia de una aplicación web.

db=mysql.connector(host='localhost', user='root', passwd='',db='my_garden')

login= login_manager('my_garden')

@app.route('/')
def index():
   
    return render_template('index.html')

if __name__ == '__main__':  #validar el archivo principal para correr la aplicacion
    app.run(debug=True)# Modo de depuracion activado (debug=True)
    
 