from manejo_archivos import guardar_datos


def agregar_contacto(contactos):
    print("Agregando un nuevo contacto...")
    nombre = input("Ingrese el nombre: ")
    try:
        telefono = int(input("Ingrese el número de teléfono: "))
    except ValueError:
        print("Por favor, ingrese un número de teléfono válido.")
        return agregar_contacto(contactos)
    email = input("Ingrese el correo electrónico: ")
    try:
        edad = int(input("Ingrese la edad: "))
    except ValueError:
        print("Por favor, ingrese una edad válida.")
        return agregar_contacto(contactos)
    residencia = input("Ingrese la residencia: ")

    nuevo_contacto = {
        "nombre": nombre.lower(),
        "telefono": telefono,
        "email": email.lower(),
        "edad": edad,
        "residencia": residencia.lower()
    }
    
    contactos.append(nuevo_contacto)
    print("Contacto agregado exitosamente.")
    guardar_datos(contactos)
    return contactos

def buscar_por_nombre(contactos, nombre):
    contactos_encontrados = []
    len_nombre = len(nombre)
    for contacto in contactos:
        if contacto["nombre"] == nombre.lower():
            contactos_encontrados.append(contacto)
        elif contacto["nombre"][:len_nombre] == nombre.lower():
            contactos_encontrados.append(contacto)
    print(f"Los contactos encontrados con el nombre '{nombre}':")
    for contacto in contactos_encontrados:
        print(f" - {contacto['nombre']} (Numero de telefono: {contacto['telefono']}) (Email: {contacto['email']})")

def buscar_por_telefono(contactos, telefono):
    telefonos_encontrados = []
    len_telefono = len(telefono)
    for contacto in contactos:
        if contacto["telefono"] == telefono:
            telefonos_encontrados.append(contacto)
        else:
            if contacto["telefono"][:len_telefono] == telefono:
                telefonos_encontrados.append(contacto)
    print(f"Los contactos encontrados con el número de teléfono '{telefono}':")
    for contacto in telefonos_encontrados:
        print(f" - Nombre: {contacto['nombre']} (Teléfono: {contacto['telefono']}) (Email: {contacto['email']})")

def mostrar_promedio_edad(contactos):
    edad = 0
    for contacto in contactos:
        edad += contacto["edad"]
    promedio = edad / len(contactos) if contactos else 0
    print(f"El promedio de edad es: {promedio}")


def mostrar_todos_los_contactos(contactos):
    for contacto in contactos:
        print(f" - {contacto['nombre']} - ({contacto['telefono']}) - {contacto['email']} - {contacto['edad']} años - {contacto['residencia']}")
