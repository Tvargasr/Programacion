import random

def pedir_palabras(numero_palabras):
    # Pedir al usuario que ingrese 15 palabras para la sopa de letras
    palabras = []
    for i in range(numero_palabras):
        palabra = input(f"Ingresa la palabra {i + 1}: ")
        if " " in palabra:
            print("Las palabras no pueden contener espacios. Intenta de nuevo.")
            return pedir_palabras(numero_palabras)
        
        palabras.append(palabra)
    return palabras

def vecinos(pos):
    # Devuelve las posiciones vecinas (8 direcciones) de una posición dada.
    fila, col = pos
    for df in (-1, 0, 1):
        for dc in (-1, 0, 1):
            yield (fila + df, col + dc)

def validar_choque_palabras(posiciones_ocupadas, nuevas_posiciones):
    # Evita que las palabras se toquen.
    for pos in nuevas_posiciones:
        for vecino in vecinos(pos):
            if vecino in posiciones_ocupadas:
                return True
    return False

def colocar_palabras_en_matriz(matriz, palabras):
    # Coloca las palabras en la matriz de la sopa de letras, asegurando que no se toquen entre sí.
    dicc_palabras = {}
    direcciones = ['horizontal', 'vertical', 'diagonal']
    direccion_palabra = ['invertida', 'normal']
    posiciones_ocupadas = set()
    for palabra in palabras:
        palabra_colocada = False
        while not palabra_colocada:
            direccion = random.choice(direcciones)
            direccion_palabra = random.choice(direccion_palabra)
            fila = random.randint(0, 49)
            columna = random.randint(0, 49)

            # Direccion Horizontal
            if direccion == 'horizontal':
                if direccion_palabra == 'normal':
                    if columna + len(palabra) <= 50:
                        nuevas_posiciones = [(fila, columna + i) for i in range(len(palabra))]
                        if not validar_choque_palabras(posiciones_ocupadas, nuevas_posiciones):
                            for i, (f, c) in enumerate(nuevas_posiciones):
                                matriz[f][c] = palabra[i]
                                posiciones_ocupadas.add((f, c))
                            palabra_colocada = True
                            dicc_palabras[palabra] = (fila, columna, direccion, direccion_palabra)
                else:
                    if columna - len(palabra) >= -1:
                        nuevas_posiciones = [(fila, columna - i) for i in range(len(palabra))]
                        if not validar_choque_palabras(posiciones_ocupadas, nuevas_posiciones):
                            for i, (f, c) in enumerate(nuevas_posiciones):
                                matriz[f][c] = palabra[i]
                                posiciones_ocupadas.add((f, c))
                            palabra_colocada = True
                            dicc_palabras[palabra] = (fila, columna, direccion, direccion_palabra)

            # Direccion Vertical
            elif direccion == 'vertical':
                if direccion_palabra == 'normal':
                    if fila + len(palabra) <= 50:
                        nuevas_posiciones = [(fila + i, columna) for i in range(len(palabra))]
                        if not validar_choque_palabras(posiciones_ocupadas, nuevas_posiciones):
                            for i, (f, c) in enumerate(nuevas_posiciones):
                                matriz[f][c] = palabra[i]
                                posiciones_ocupadas.add((f, c))
                            palabra_colocada = True
                            dicc_palabras[palabra] = (fila, columna, direccion, direccion_palabra)
                else:
                    if fila - len(palabra) >= -1:
                        nuevas_posiciones = [(fila - i, columna) for i in range(len(palabra))]
                        if not validar_choque_palabras(posiciones_ocupadas, nuevas_posiciones):
                            for i, (f, c) in enumerate(nuevas_posiciones):
                                matriz[f][c] = palabra[i]
                                posiciones_ocupadas.add((f, c))
                            palabra_colocada = True
                            dicc_palabras[palabra] = (fila, columna, direccion, direccion_palabra)

            # Direccion Diagonal
            else:
                if direccion_palabra == 'normal':
                    if fila + len(palabra) <= 50 and columna + len(palabra) <= 50:
                        nuevas_posiciones = [(fila + i, columna + i) for i in range(len(palabra))]
                        if not validar_choque_palabras(posiciones_ocupadas, nuevas_posiciones):
                            for i, (f, c) in enumerate(nuevas_posiciones):
                                matriz[f][c] = palabra[i]
                                posiciones_ocupadas.add((f, c))
                            palabra_colocada = True
                            dicc_palabras[palabra] = (fila, columna, direccion, direccion_palabra)
                else:
                    if fila - len(palabra) >= -1 and columna - len(palabra) >= -1:
                        nuevas_posiciones = [(fila - i, columna - i) for i in range(len(palabra))]
                        if not validar_choque_palabras(posiciones_ocupadas, nuevas_posiciones):
                            for i, (f, c) in enumerate(nuevas_posiciones):
                                matriz[f][c] = palabra[i]
                                posiciones_ocupadas.add((f, c))
                            palabra_colocada = True
                            dicc_palabras[palabra] = (fila, columna, direccion, direccion_palabra)
    
    return posiciones_ocupadas