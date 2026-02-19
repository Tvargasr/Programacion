class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_persona(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar_mascota(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}"
    
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_vehiculo(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"
    
