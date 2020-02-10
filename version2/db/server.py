from flask import Flask, jsonify,request
from flask_cors import CORS
#from controllers.medicion import Datos

app = Flask(__name__)
CORS(app)

@app.route('/listarDatos', methods=['GET'])
def getAll():
    return (Datos.list())

@app.route('/listarDatos', methods=['POST'])
def postOne():
    body = request.json
    return (Datos.create(body))

app.run(port=5000, debug=True)