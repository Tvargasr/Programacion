#Tarea Programada 3 - Sopa de Letras
#Autor: Tomás Vargas

from matriz_sopa import generar_matriz_sopa, imprimir_matriz_resuelta
from palabras_sopa import pedir_palabras, colocar_palabras_en_matriz

# Función principal del programa
def main():
    while True:
        print("Sopa de Letras")
        print("1. Generar Sopa de Letras")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            # Generar la matriz de la sopa de letras, pedir las palabras, colocarlas en la matriz y mostrar el resultado
            matriz = generar_matriz_sopa()
            palabras = pedir_palabras()
            posiciones_palabras = colocar_palabras_en_matriz(matriz, palabras)
            imprimir_matriz_resuelta(matriz, posiciones_palabras)
        elif opcion == '2':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1 o 2.")

if __name__ == "__main__":
    main()