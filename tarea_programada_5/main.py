from manejo_archivos import cargar_datos_csv, cargar_datos_json, guardar_datos
from manejo_contactos import agregar_contacto, buscar_por_nombre, buscar_por_telefono, mostrar_promedio_edad, mostrar_todos_los_contactos

def menu():
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
            menu_cargar_datos()
        elif opcion == "2":
            agregar_contacto()
        elif opcion == "3":
            buscar_por_nombre()
        elif opcion == "4":
            buscar_por_telefono()
        elif opcion == "5":
            mostrar_promedio_edad()
        elif opcion == "6":
            mostrar_todos_los_contactos()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def menu_cargar_datos():
    print("Que tipo de archivo desea cargar?")
    print("1. CSV")
    print("2. JSON")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        cargar_datos_csv()
    elif opcion == "2":
        cargar_datos_json()
    else:
        print("Opción no válida. Por favor, intente de nuevo.")