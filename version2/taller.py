from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')


Datos_List = [
    {'Usuario':1040757225, 'Temperatura':'20', 
    'Humedad':'50', 'GPS':'O75°33,48.92-N6°15,6.62'}
]

@app.route('/listar', methods = ['GET'])
def listar():
    Datos_List= requests.get('http://localhost:5000/listar').json()
    return render_template('listar.html', list = Datos_List)

@app.route('/formulario', methods = ['GET'])
def formulario():
    return render_template('formulario.html')

@app.route('/guardarDato', methods = ['POST'])
def guardarParticipante():
    dato = dict(request.values)
    dato['Usuario'] = str(dato['Usuario'])
    requests.post('http://localhost:5000/listarDatos', json=dato)
    #Datos_List.append(dato)
    return render_template('formulario.html')



app.run(port=8000, debug=True)