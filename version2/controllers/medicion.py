from flask import jsonify, request
from db.db import cnx

class Datos():
    global cur 
    cur= cnx.cursor()

    def list():
        lista= []
        cur.execute("SELECT * FROM Datos")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            #Create a zip object from two lists
            registro = zip(columns,row)
            #Create a dictionary  from zip object
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close

    def create(body):
        data = (body['Usuario'],body['Temperatura'],body['Humedad'],body['GPS'])
        sql = "INSERT INTO mediciones(Usuario, Temperatura, Humedad, GPS) VALUES(%s,%s,%s,%s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado':"Insertado"}, 200
