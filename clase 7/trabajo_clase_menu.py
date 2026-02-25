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
        print("4. Asociar Vehículo a Persona")
        print("5. Mostrar Personas")
        print("6. Mostrar Mascotas")
        print("7. Mostrar Vehículos")
        print("8. Mostrar Todo")
        print("9. Salir")
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
            print("\n--- Personas disponibles ---")
            for i, persona in enumerate(personas):
                print(f"{i}. {persona.get_persona()[0]}")
            indice_persona = int(input("Seleccione el índice de la persona: "))
            
            print("\n--- Vehículos disponibles ---")
            for i, vehiculo in enumerate(vehiculos):
                print(f"{i}. {vehiculo.get_vehiculo()[0]} {vehiculo.get_vehiculo()[1]}")
            indice_vehiculo = int(input("Seleccione el índice del vehículo: "))
            
            if 0 <= indice_persona < len(personas) and 0 <= indice_vehiculo < len(vehiculos):
                personas[indice_persona].set_vehiculo(vehiculos[indice_vehiculo])
                vehiculos[indice_vehiculo].set_dueno(personas[indice_persona])
                print("Asociación realizada exitosamente.")
            else:
                print("Índices inválidos.")

        elif opcion == '5':
            print("\n--- Personas ---")
            for persona in personas:
                print(persona.__str__())

        elif opcion == '6':
            print("\n--- Mascotas ---")
            for mascota in mascotas:
                print(mascota.__str__())

        elif opcion == '7':
            print("\n--- Vehículos ---")
            for vehiculo in vehiculos:
                print(vehiculo.__str__())

        elif opcion == '8':
            print("\n--- Personas ---")
            for persona in personas:
                print(persona.__str__())
            print("\n--- Mascotas ---")
            for mascota in mascotas:
                print(mascota.__str__())
            print("\n--- Vehículos ---")
            for vehiculo in vehiculos:
                print(vehiculo.__str__())

        elif opcion == '9':
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()