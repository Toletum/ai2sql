"""

"""
import time
import sqlite3
import json

from ollama import Client

client = Client(host='http://localhost:11434')

# Define el prompt y el modelo

ini = time.time()

response = client.chat(model='mistral:7b', format='json',
                       messages=[
    {
        'role': 'system',
        'content': """Tengo una base de datos llamada JCS con la siguente estructura:
 * Tabla Cliente con los campos: dni, nombre, apellidos
 * Tabla Direccion: dni, via, codigo
 * Tabla CodigoPostal: codigo, provincia, municipio

Las relaciones entre Tablas son:
 * Tabla Cliente y Tabla Direccion: campo dni
 * Tabla Direccion y Tabla CodigoPostal: campo codigo

El motor de base de datos es sqlite. Quiero que me des el SQL
"""
    },
    {
        'role': 'user',
        'content': "listar todos los clientes del municipio = CiudadA",
    },
],
                       stream=False)

end = time.time()
try:
    data = json.loads(response['message']['content'])
except Exception as ex:
    print(ex)
    quit(1)
query = None
if "sql" in data:
    query = data['sql']
if "SQL" in data:
    query = " ".join(data['SQL'])
if "query" in data:
    query = data['query']
if query:
    rint(query)
    db = sqlite3.connect("db.db")
    cursor = db.cursor()
    cursor.execute(query)
    for fila in cursor.fetchall():
        print(fila)
    db.close()
else:
    print(response['message']['content'])

print(f" total:  {(end - ini)}")
