alfabeto = "abcdefghijklmnopqrstuvwxyz"
def encriptar(texto, clave):
    resultado = ""
    for letra in texto:
        if letra in alfabeto:
            indice = (alfabeto.index(letra) + clave) % len(alfabeto)
            resultado += alfabeto[indice]
        else:
            resultado += letra
    return resultado

def desencriptar(texto, clave):
    resultado = ""
    for letra in texto:
        if letra in alfabeto:
            indice = (alfabeto.index(letra) - clave) % len(alfabeto)
            resultado += alfabeto[indice]
        else:
            resultado += letra
    return resultado