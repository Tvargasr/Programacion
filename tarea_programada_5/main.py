#Tomas Vargas
#Tarea Programada 5 - Agenda de Contactos

from manejo_archivos import cargar_datos_csv, cargar_datos_json
from manejo_contactos import agregar_contacto, buscar_por_nombre, buscar_por_telefono, mostrar_promedio_edad, mostrar_todos_los_contactos



def menu():
    contactos = []
    while True:
        print("---Agenda de contactos---")
        print("1. Cargar Datos de un archivo")
        print("2. Agregar un nuevo contacto")
        print("3. Buscar por nombre")
        print("4. Buscar por número de teléfono")
        print("5. Mostrar el promedio de edad de los contactos")
        print("6. Mostrar todos los contactos")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("Que tipo de archivo desea cargar?")
            print("1. CSV")
            print("2. JSON")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                contactos = cargar_datos_csv()
            elif opcion == "2":
                contactos = cargar_datos_json()
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        elif opcion == "2":
            contactos = agregar_contacto(contactos)
        elif opcion == "3":
            buscar_por_nombre(contactos, nombre=input("Ingrese el nombre a buscar: "))
        elif opcion == "4":
            try:
                telefono = int(input("Ingrese el número de teléfono a buscar: "))
            except ValueError:                
                print("Por favor, ingrese un número de teléfono válido.")
                return menu()
            buscar_por_telefono(contactos, telefono)
        elif opcion == "5":
            mostrar_promedio_edad(contactos)
        elif opcion == "6":
            mostrar_todos_los_contactos(contactos)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()