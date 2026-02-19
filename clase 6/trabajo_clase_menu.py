from trabajo_clase_modulos import Persona, Mascota, Vehiculo
personas = []
mascotas = []
vehiculos = []


def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Persona")
        print("2. Agregar Mascota")
        print("3. Agregar Vehículo")
        print("4. Mostrar Personas")
        print("5. Mostrar Mascotas")
        print("6. Mostrar Vehículos")
        print("7. Mostrar Todo")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre = input("Ingrese el nombre de la persona: ")
            edad = input("Ingrese la edad de la persona: ")
            personas.append(Persona(nombre, edad))

        elif opcion == '2':
            nombre = input("Ingrese el nombre de la mascota: ")
            tipo = input("Ingrese el tipo de mascota: ")
            mascotas.append(Mascota(nombre, tipo))

        elif opcion == '3':
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            año = input("Ingrese el año del vehículo: ")
            vehiculos.append(Vehiculo(marca, modelo, año))

        elif opcion == '4':
            for persona in personas:
                print(persona.mostrar_persona())

        elif opcion == '5':
            for mascota in mascotas:
                print(mascota.mostrar_mascota())

        elif opcion == '6':
            for vehiculo in vehiculos:
                print(vehiculo.mostrar_vehiculo())

        elif opcion == '7':
            print("\n--- Personas ---")
            for persona in personas:
                print(persona.mostrar_persona())
            print("\n--- Mascotas ---")
            for mascota in mascotas:
                print(mascota.mostrar_mascota())
            print("\n--- Vehículos ---")
            for vehiculo in vehiculos:
                print(vehiculo.mostrar_vehiculo())

        elif opcion == '8':
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()