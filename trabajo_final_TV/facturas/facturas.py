import json
import datetime
import os
from carga_de_datos import cargar_direccion

class Factura:
    def __init__(self):
        self.productos = []
        self.total = 0.0
    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio
    def mostrar_factura(self):
        print("Factura:")
        for producto in self.productos:
            print(f"{producto.nombre} - ${producto.precio}")
        print(f"Total a pagar: ${self.total}")
    def generar_factura(self):
        direccion = cargar_direccion()
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"factura_{fecha_hora}.json"
        ruta_archivo = os.path.join(direccion, 'facturas', nombre_archivo)
        factura_data = {
            "productos": [{"nombre": producto.nombre, "precio": producto.precio} for producto in self.productos],
            "total": self.total
        }
        with open(ruta_archivo, 'w') as archivo_json:
            json.dump(factura_data, archivo_json, indent=4)
        print(f"Factura guardada en {ruta_archivo}")

