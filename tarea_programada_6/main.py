from creacion_operaciones import *
from archivos import *

def main():
    while True:
        print("Menu: para salir, digite 'salir'\n")
        try:
            n_sumas = int(input("Numero de sumas: "))
            if n_sumas == "salir":
                break
            n_restas = int(input("Numero de restas: "))
            if n_restas == "salir":
                break
            n_multiplicaciones = int(input("Numero de multiplicaciones: "))
            if n_multiplicaciones == "salir":
                break
            n_divisiones = int(input("Numero de divisiones: "))
            if n_divisiones == "salir":
                break
            operaciones = []
            operaciones.append(creacion_sumas(n_sumas))
            operaciones.append(creacion_restas(n_restas))
            operaciones.append(creacion_multiplicaciones(n_multiplicaciones))
            operaciones.append(creacion_divisiones(n_divisiones))
            print(operaciones)
            print(archivo_respuestas(operaciones))
            print(archivo_sin_respuestas(operaciones))
            
        
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
