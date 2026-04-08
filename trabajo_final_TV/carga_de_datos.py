import csv
import json
import os
from videojuegos import Catalogo

def cargar_direccion():
    direccion = os.path.dirname(os.path.abspath(__file__))
    return direccion

def cargar_datos_csv():
    catalogo = Catalogo()
    direccion = cargar_direccion()
    with open(os.path.join(direccion, 'data', 'catalogo.csv'), mode='r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            catalogo.append(fila)
    print("Datos cargados desde el archivo CSV.")
    return catalogo
    
def cargar_datos_json():
    catalogo = Catalogo()
    direccion = cargar_direccion()
    with open(os.path.join(direccion, 'data', 'catalogo.json'), mode='r') as archivo_json:
        catalogo = json.load(archivo_json)
    print("Datos cargados desde el archivo JSON.")
    return catalogo

def guardar_datos(catalogo):
    direccion = cargar_direccion()
    #CSV
    with open(os.path.join(direccion, 'data', 'catalogo.csv'), mode='w', newline='') as archivo_csv:
        campos = ['nombre', 'telefono', 'email', 'edad', 'residencia']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for contacto in catalogo:
            escritor_csv.writerow(contacto)
    #JSON
    with open(os.path.join(direccion, 'data', 'catalogo.json'), mode='w') as archivo_json:
        json.dump(catalogo, archivo_json, indent=4)
    print("Datos guardados en los archivos CSV y JSON.")