class Videojuego:
    def __init__ (self, identificador, nombre, categoria, precio, ESRB_rating, cant_stock, plataforma):
        self.identificador = identificador
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.ESRB_rating = ESRB_rating
        self.cant_stock = cant_stock
        self.plataforma = plataforma
    
    def __str__(self):
        print(f"ID: {self.identificador}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoria: {self.categoria}")
        print(f"Precio: {self.precio}")
        print(f"ESRB Rating: {self.ESRB_rating}")
        print(f"Cantidad en stock: {self.cant_stock}")
        print(f"Plataforma: {self.plataforma}")

class VideojuegoPS5(Videojuego):
    def __init__ (self, identificador, nombre, categoria, precio, ESRB_rating, cant_stock):
        super().__init__(identificador, nombre, categoria, precio, ESRB_rating, cant_stock, "PS5")
    
class VideojuegoXbox(Videojuego):
    def __init__ (self, identificador, nombre, categoria, precio, ESRB_rating, cant_stock):
        super().__init__(identificador, nombre, categoria, precio, ESRB_rating, cant_stock, "Xbox")

class VideojuegoNintendo(Videojuego):
    def __init__ (self, identificador, nombre, categoria, precio, ESRB_rating, cant_stock):
        super().__init__(identificador, nombre, categoria, precio, ESRB_rating, cant_stock, "Nintendo")

class Catalogo:
    def __init__(self):
        self.videojuegos = []

    def agregar_videojuego(self, videojuego):
        self.videojuegos.append(videojuego)

    def eliminar_videojuego(self, videojuego):
        if videojuego in self.videojuegos:
            self.videojuegos.remove(videojuego)

    def mostrar_catalogo(self):
        for videojuego in self.videojuegos:
            print(videojuego)