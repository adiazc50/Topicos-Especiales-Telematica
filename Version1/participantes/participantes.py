from flask import Flask
from flask_cors import CORS
from datetime import date
from datetime import datetime
from flask import request, Response, jsonify, render_template

app = Flask(__name__, template_folder='templates')
CORS(app)

Datos_List = [
    {'Usuario':1040757225, 'Temperatura':'20', 
    'Humedad':'50', 'GPS':'O75°33,48.92-N6°15,6.62'}
]


@app.route('/formulario', methods = ['GET'])
def formulario():
    return render_template('formulario.html')

@app.route('/formulario', methods = ['POST'])
def guardarParticipante():
    dato = dict(request.values)
    dato['Usuario'] = str(dato['Usuario'])
    Datos_List.append(dato)
    return render_template('formulario.html')

@app.route('/listar', methods = ['GET'])
def listar():
    return render_template('listar.html', list = Datos_List)

app.run(port=5000, debug=True)