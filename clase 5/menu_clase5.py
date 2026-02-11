import volumenes as v
import encriptacion as e

def menu_volumenes():
    print("")
    print("Calculadora de Volúmenes")
    print("1. Cubo")
    print("2. Esfera")
    print("3. Cilindro")
    print("4. Cono")
    print("5. Paralelepípedo")
    print("")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        lado = float(input("Ingrese la longitud del lado del cubo: "))
        volumen = v.cubo(lado)
        print(f"El volumen del cubo es: {volumen}")
    elif opcion == 2:
        radio = float(input("Ingrese el radio: "))
        volumen = v.esfera(radio)
        print(f"El volumen de la esfera es: {volumen}")
    elif opcion == 3:
        radio = float(input("Ingrese el radio: "))
        altura = float(input("Ingrese la altura: "))
        volumen = v.cilindro(radio, altura)
        print(f"El volumen del cilindro es: {volumen}")
    elif opcion == 4:
        radio = float(input("Ingrese el radio: "))
        altura = float(input("Ingrese la altura: "))
        volumen = v.cono(radio, altura)
        print(f"El volumen del cono es: {volumen}")
    elif opcion == 5:
        longitud = float(input("Ingrese la longitud: "))
        ancho = float(input("Ingrese el ancho: "))
        altura = float(input("Ingrese la altura: "))
        volumen = v.paralepipedo(longitud, ancho, altura)
        print(f"El volumen del paralelepípedo es: {volumen}")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

def menu_encriptacion():
    print("")
    print("Calculadora de Encriptación")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        texto = input("Ingrese el texto a encriptar: ")
        clave = int(input("Ingrese la clave de encriptación (número de desplazamiento): "))
        resultado = e.encriptar(texto, clave)
        print(f"Texto encriptado: {resultado}")
        
    elif opcion == 2:
        texto = input("Ingrese el texto a desencriptar: ")
        clave = int(input("Ingrese la clave de desencriptación (número de desplazamiento): "))
        resultado = e.desencriptar(texto, clave)
        print(f"Texto desencriptado: {resultado}")
        
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")

def menu_principal():
    while True:
        print("")
        print("Menú Principal")
        print("1. Calculadora de Volúmenes")
        print("2. Calculadora de Encriptación")
        print("3. Salir")
        print("")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            menu_volumenes()
        elif opcion == 2:
            menu_encriptacion()
        elif opcion == 3:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

menu_principal()