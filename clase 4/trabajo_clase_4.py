# contador de palabras 
def eliminar_puntuacion(texto):
    puntuacion = "!()-[]{};:'\"\,<>./?@#$%^&*_~"
    for character in texto:
        if character in puntuacion:
            texto = texto.replace(character, "")
    return texto

def contar_palabras():
    # solicitar texto al usuario
    palabras = input("Ingrese su texto aqui: ")
    # eliminar puntuacion y convertir a minusculas
    palabras = eliminar_puntuacion(palabras).lower()
    # dividir el texto en palabras
    lista_palabras = palabras.split()
    ignorar_palabras = ["el", "la", "de", "y", "a", "un", "una"]
    # contar palabras
    contador = {}
    for palabra in lista_palabras:
        if palabra not in ignorar_palabras:
            if palabra in contador:
                contador[palabra] += 1
            else:
                contador[palabra] = 1
                
    # cantidad total de palabras
    total_palabras = sum(contador.values())
    print(f"Cantidad total de palabras (sin contar las ignoradas): {total_palabras}")

    # cantidad de palabras unicas
    palabras_unicas = len(contador)
    print(f"Cantidad de palabras unicas: {palabras_unicas}")

    # 5 palabras mas comunes
    palabras_comunes = sorted(contador.items(), key=lambda x: x[1]) [-5:]
    print("Las 5 palabras más comunes son:")
    for palabra, cantidad in palabras_comunes:
        print(f"{palabra}: {cantidad}")

contar_palabras()