import json
import csv
import os

def lectura_csv(csv_archivo):
    personas = []
    with open(csv_archivo, "r") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            persona = {
                "nombre": fila["nombre"],
                "salario": float(fila["salario"]),
                "edad": float(fila["edad"]),
                "peso": float(fila["peso"])
            }
            personas.append(persona)
    return personas


def lectura_json(json_archivo):
    with open(json_archivo, "r") as archivo:
        personas = json.load(archivo)
    return personas

def promedio_edad(personas):
    total_edad = 0
    for persona in personas:
        total_edad += persona["edad"]
    promedio = total_edad / len(personas)
    return promedio

def promedio_salario(personas):
    total_salario = 0
    for persona in personas:
        total_salario += persona["salario"]
    promedio = total_salario / len(personas)
    return promedio

def promedio_peso(personas):
    total_peso = 0
    for persona in personas:
        total_peso += persona["peso"]
    promedio = total_peso / len(personas)
    return promedio

def eleccion():
    while True:
        direccion = os.getcwd()
        direccion_csv = os.path.join(direccion, "personas.csv")
        direccion_json = os.path.join(direccion, "personas.json")

        print("1. CSV")
        print("2. JSON")
        opcion = input("Ingrese una opción: ")
        if opcion in ["1", "2"]:
            if opcion == "1":
                print("Has seleccionado CSV.")
                personas_csv = lectura_csv(direccion_csv)
                print(personas_csv)
                print(f"El promedio de edad es: {promedio_edad(personas_csv)}")
                print(f"El promedio de salario es: {promedio_salario(personas_csv)}")
                print(f"El promedio de peso es: {promedio_peso(personas_csv)}")
            else:
                print("Has seleccionado JSON.")
                personas_json = lectura_json(direccion_json)
                print(personas_json)
                print(f"El promedio de edad es: {promedio_edad(personas_json)}")
                print(f"El promedio de salario es: {promedio_salario(personas_json)}")
                print(f"El promedio de peso es: {promedio_peso(personas_json)}")
        else:
            break

if __name__ == "__main__":
    eleccion()