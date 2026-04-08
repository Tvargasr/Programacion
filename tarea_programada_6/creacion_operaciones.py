import random

def creacion_sumas(n_sumas):
    sumas = []
    for _ in range(n_sumas):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        sumas.append((num1, " + ", num2, num1 + num2))
    return sumas

def creacion_restas(n_restas):
    restas = []
    for _ in range(n_restas):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        restas.append((num1, " - ", num2, num1 - num2))
    return restas

def creacion_multiplicaciones(n_multiplicaciones):
    multiplicaciones = []
    for _ in range(n_multiplicaciones):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        multiplicaciones.append((num1, " * ", num2, num1 * num2))
    return multiplicaciones

def creacion_divisiones(n_divisiones):
    divisiones = []
    for _ in range(n_divisiones):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        divisiones.append((num1, " / ", num2, num1 / num2))
    return divisiones