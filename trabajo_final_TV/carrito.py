class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)

    def mostrar_carrito(self):
        for producto in self.productos:
            print(f"{producto.nombre} - ${producto.precio}")
        print(f"Total: ${self.calcular_total()}")