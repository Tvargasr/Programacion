from carga_de_datos import *
from trabajo_final_TV import carrito
from videojuegos import *
from carrito import *
from facturas.facturas import *



def menu():
    carrito = Carrito()
    while True:
        print("Catalogo de videojuegos")
        print("1. Agregar videojuego")
        print("2. Eliminar videojuego")
        print("3. Mostrar catalogo")
        print("4. Menu carrito de compras")
        print("5. Menu factura")
        print("6. Cargar datos del catalogo")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            catalogo.agregar_videojuego()
        elif opcion == "2":
            catalogo.eliminar_videojuego()
        elif opcion == "3":
            catalogo.mostrar_catalogo()
        elif opcion == "4":
            menu_carrito()
        elif opcion == "5":
            menu_factura()
        elif opcion == "6":
            catalogo = menu_cargar_datos()
        elif opcion == "7":
            print("Gracias vuelva pronto!")
            guardar_datos(catalogo)
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def menu_cargar_datos():
    print("Cargar datos del catalogo")
    print("1. Cargar desde CSV")
    print("2. Cargar desde JSON")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        catalogo = cargar_datos_csv()
        return catalogo
    elif opcion == "2":
        catalogo = cargar_datos_json()
        return catalogo
    else:
        print("Opción no válida, por favor intente de nuevo.")


def menu_carrito():
    print("Carrito de compras")
    print("1. Ver productos en el carrito")
    print("2. Eliminar producto del carrito")
    print("3. Mostrar carrito")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        carrito.mostrar_carrito()
    elif opcion == "2":
        carrito.eliminar_producto()
    elif opcion == "3":
        carrito.mostrar_carrito()
    elif opcion == "4":
        return
    else:
        print("Opción no válida, por favor intente de nuevo.")

def menu_factura():
    factura = Factura()
    print("Factura")
    print("1. Ver productos en la factura")
    print("2. Generar factura")
    print("3. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        factura.mostrar_factura()
    elif opcion == "2":
        factura.generar_factura()
    elif opcion == "3":
        return
    else:
        print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    menu()