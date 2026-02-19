import random
import string

# Generar la matriz de la sopa de letras 50 x 50 con letras aleatorias
def generar_matriz_sopa():
    matriz = []

    for _ in range(50):
        fila = [random.choice(string.ascii_lowercase) for _ in range(50)]
        matriz.append(fila)

    return matriz

# Imprimir la matriz de la sopa de letras
def imprimir_matriz_resuelta(matriz, posiciones_palabras):
    # Imprimir la matriz con colores
    for fila_idx, fila in enumerate(matriz):
        fila_str = ""
        for col_idx, letra in enumerate(fila):
            if (fila_idx, col_idx) in posiciones_palabras:
                # Colorear en verde si es parte de una palabra
                fila_str += "\033[92m" + letra + "\033[0m" + " "
            else:
                # Letras normales
                fila_str += letra + " "
        print(fila_str)