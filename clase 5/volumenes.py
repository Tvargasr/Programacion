def cubo(lado):
    return lado ** 3

def esfera(radio):
    return (4/3) * 3.1416 * radio ** 3

def cilindro(radio, altura):
    return 3.1416 * radio ** 2 * altura

def cono(radio, altura):
    return (1/3) * 3.1416 * radio ** 2 * altura

def paralepipedo(longitud, ancho, altura):
    return longitud * ancho * altura