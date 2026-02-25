#Tarea Programada 3 - Sopa de Letras
#Autor: Tomás Vargas

from matriz_sopa import generar_matriz_sopa, imprimir_matriz_resuelta, imprimir_matriz
from palabras_sopa import pedir_palabras, colocar_palabras_en_matriz

# Función principal del programa
def main():
    palabras = []
    matriz = []
    while True:
        print("Sopa de Letras")
        print("1. Ingresar palabras")
        print("2. Imprimir Sopa de Letras")
        print("3. Imprimir Sopa de Letras Resuelta")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            try:
                numero_palabras = int(input("¿Cuántas palabras deseas ingresar? (máximo 15): "))
                if numero_palabras < 1 or numero_palabras > 15:
                    print("Por favor, ingresa un número entre 1 y 15.")
                else:
                    palabras = pedir_palabras(numero_palabras)
                    matriz = generar_matriz_sopa()
                    posiciones_palabras = colocar_palabras_en_matriz(matriz, palabras)
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero.")

        elif opcion == '2':
            if not palabras:
                print("Primero debes ingresar las palabras.")
            else:
                imprimir_matriz(matriz, posiciones_palabras)

        elif opcion == '3':
            if not palabras:
                print("Primero debes ingresar las palabras.")
            else:
                imprimir_matriz_resuelta(matriz, posiciones_palabras)

        elif opcion == '4':
            print("¡Gracias por jugar! Hasta luego.")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1 o 2.")

if __name__ == "__main__":
    main()