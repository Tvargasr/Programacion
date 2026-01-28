#Tomas Vargas - calculadora.py
def conversion_validacion(operacion):
    lista_operacion = []
    for caracter in operacion:
        if caracter not in "0123456789+-*/. ":
            return False
        else:
            try:
                lista_operacion.append(float(caracter))
            except ValueError:
                lista_operacion.append(caracter)

    for i in range(len(lista_operacion)-1):
        if (isinstance(lista_operacion[i], str) and isinstance(lista_operacion[i+1], str)):
            return False
        
        if (isinstance(lista_operacion[i], float) and isinstance(lista_operacion[i+1], float)):
            return False
    
    return lista_operacion

def calculadora():
    operacion = ""
    while operacion != "salir":
        operacion = input("Ingrese la operacion 'salir' para salir: ")
        if operacion != "salir":
            lista_operacion = conversion_validacion(operacion)
            if lista_operacion != False:
                resultado = lista_operacion[0]
                i = 1
                while i < len(lista_operacion):
                    operador = lista_operacion[i]
                    siguiente_numero = lista_operacion[i+1]
                    if operador == "+":
                        resultado += siguiente_numero
                    elif operador == "-":
                        resultado -= siguiente_numero
                    elif operador == "*":
                        resultado *= siguiente_numero
                    elif operador == "/":
                        if siguiente_numero != 0:
                            resultado /= siguiente_numero
                        else:
                            print("Error: Division por cero")
                            break
                    i += 2
                else:
                    print("El resultado es:", resultado)
            else:
                print("Operacion no valida")

calculadora()