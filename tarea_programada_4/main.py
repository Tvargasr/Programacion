from empleados import Administrador, Conserje, Guardian, Veterinario
from metodos_transporte import Bicicleta, Cuadraciclo, Patineta
from animales import Aguila, Leon, PezPayaso, Rana, Serpiente


empleados = []
transportes = []
animales = []


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero.")


def listar_elementos(titulo, lista):
    print(f"\n--- {titulo} ---")
    if not lista:
        print("No hay registros.")
        return
    for indice, elemento in enumerate(lista, start=1):
        print(f"{indice}. {elemento}")


def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Agregar empleado")
        print("2. Lista de empleados")
        print("3. Agregar método de transporte")
        print("4. Lista de métodos de transporte")
        print("5. Agregar animal")
        print("6. Lista de animales")
        print("7. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            menu_empleados()
        elif opcion == "2":
            listar_elementos("Empleados", empleados)
        elif opcion == "3":
            menu_transporte()
        elif opcion == "4":
            listar_elementos("Métodos de transporte", transportes)
        elif opcion == "5":
            menu_animales()
        elif opcion == "6":
            listar_elementos("Animales", animales)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_empleados():
    while True:
        print("\n--- Menú Empleados ---")
        print("1. Agregar administrador")
        print("2. Agregar guardián")
        print("3. Agregar conserje")
        print("4. Agregar veterinario")
        print("5. Regresar")
        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                edad = leer_entero("Edad: ")
                departamento = input("Departamento: ")
                empleados.append(Administrador(nombre, edad, departamento))
                print("Administrador agregado correctamente.")
            elif opcion == "2":
                nombre = input("Nombre: ")
                edad = leer_entero("Edad: ")
                turno = input("Turno: ")
                empleados.append(Guardian(nombre, edad, turno))
                print("Guardián agregado correctamente.")
            elif opcion == "3":
                nombre = input("Nombre: ")
                edad = leer_entero("Edad: ")
                area = input("Área: ")
                empleados.append(Conserje(nombre, edad, area))
                print("Conserje agregado correctamente.")
            elif opcion == "4":
                nombre = input("Nombre: ")
                edad = leer_entero("Edad: ")
                especialidad = input("Especialidad: ")
                empleados.append(Veterinario(nombre, edad, especialidad))
                print("Veterinario agregado correctamente.")
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as error:
            print(f"Error: {error}")


def menu_transporte():
    while True:
        print("\n--- Menú Transporte ---")
        print("1. Agregar bicicleta")
        print("2. Agregar cuadraciclo")
        print("3. Agregar patineta")
        print("4. Regresar")
        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                tipo = input("Tipo: ")
                capacidad = leer_entero("Capacidad: ")
                marca = input("Marca: ")
                transportes.append(Bicicleta(tipo, capacidad, marca))
                print("Bicicleta agregada correctamente.")
            elif opcion == "2":
                tipo = input("Tipo: ")
                capacidad = leer_entero("Capacidad: ")
                modelo = input("Modelo: ")
                transportes.append(Cuadraciclo(tipo, capacidad, modelo))
                print("Cuadraciclo agregado correctamente.")
            elif opcion == "3":
                tipo = input("Tipo: ")
                capacidad = leer_entero("Capacidad: ")
                color = input("Color: ")
                transportes.append(Patineta(tipo, capacidad, color))
                print("Patineta agregada correctamente.")
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as error:
            print(f"Error: {error}")


def menu_animales():
    while True:
        print("\n--- Menú Animales ---")
        print("1. Agregar serpiente")
        print("2. Agregar león")
        print("3. Agregar águila")
        print("4. Agregar pez payaso")
        print("5. Agregar rana")
        print("6. Regresar")
        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                edad = leer_entero("Edad: ")
                tipo_escama = input("Tipo de escama: ")
                animales.append(Serpiente(nombre, edad, tipo_escama))
                print("Serpiente agregada correctamente.")
            elif opcion == "2":
                nombre = input("Nombre: ")
                edad = leer_entero("Edad: ")
                tipo_pelo = input("Tipo de pelo: ")
                animales.append(Leon(nombre, edad, tipo_pelo))
                print("León agregado correctamente.")
            elif opcion == "3":
                nombre = input("Nombre: ")
                edad = leer_entero("Edad: ")
                tipo_pluma = input("Tipo de pluma: ")
                animales.append(Aguila(nombre, edad, tipo_pluma))
                print("Águila agregada correctamente.")
            elif opcion == "4":
                nombre = input("Nombre: ")
                edad = leer_entero("Edad: ")
                tipo_agua = input("Tipo de agua: ")
                animales.append(PezPayaso(nombre, edad, tipo_agua))
                print("Pez payaso agregado correctamente.")
            elif opcion == "5":
                nombre = input("Nombre: ")
                edad = leer_entero("Edad: ")
                tipo_piel = input("Tipo de piel: ")
                animales.append(Rana(nombre, edad, tipo_piel))
                print("Rana agregada correctamente.")
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    menu_principal()
