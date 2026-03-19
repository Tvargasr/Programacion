import csv
import json
import os

def cargar_direccion():
    direccion = os.path.dirname(os.path.abspath(__file__))
    return direccion

def cargar_datos_csv():
    contactos = []
    direccion = cargar_direccion()
    with open(os.path.join(direccion, 'data', 'contactos.csv'), mode='r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            contactos.append(fila)
    print("Datos cargados desde el archivo CSV.")
    return contactos
    
def cargar_datos_json():
    contactos = []
    direccion = cargar_direccion()
    with open(os.path.join(direccion, 'data', 'contactos.json'), mode='r') as archivo_json:
        contactos = json.load(archivo_json)
    print("Datos cargados desde el archivo JSON.")
    return contactos

def guardar_datos(contactos):
    direccion = cargar_direccion()
    #CSV
    with open(os.path.join(direccion, 'data', 'contactos.csv'), mode='w', newline='') as archivo_csv:
        campos = ['nombre', 'telefono', 'email', 'edad', 'residencia']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for contacto in contactos:
            escritor_csv.writerow(contacto)
    #JSON
    with open(os.path.join(direccion, 'data', 'contactos.json'), mode='w') as archivo_json:
        json.dump(contactos, archivo_json, indent=4)
    print("Datos guardados en los archivos CSV y JSON.")