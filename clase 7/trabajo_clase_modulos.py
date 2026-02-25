class Persona:
    def __init__(self, nombre, edad, vehiculo=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__vehiculo = vehiculo
        self.__corazon = Corazon()

    def get_persona(self):
        return self.__nombre, self.__edad
    
    def get_vehiculo(self):
        return self.__vehiculo
    
    def set_vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo
    
    def set_persona(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __str__(self):
        vehiculo_info = "Sí" if self.__vehiculo else "No"
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Tiene vehículo: {vehiculo_info}, Corazón: {self.__corazon.latir()}"
    
    def __len__(self):
        return len(self.__nombre) + len(str(self.__edad))
    
class Mascota:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo

    def get_mascota(self):
        return self.__nombre, self.__tipo
    
    def set_mascota(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo

    def __str__(self):
        return f"Nombre: {self.__nombre}, Tipo: {self.__tipo}"
    
    def __len__(self):
        return len(self.__nombre) + len(self.__tipo)
        
class Vehiculo:
    def __init__(self, marca, modelo, año, dueno=None):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__dueno = dueno

    def get_vehiculo(self):
        return self.__marca, self.__modelo, self.__año
    
    def get_dueno(self):
        return self.__dueno
    
    def set_dueno(self, dueno):
        self.__dueno = dueno
    
    def set_vehiculo(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def __str__(self):
        dueno_info = "Sí" if self.__dueno else "No"
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}, Tiene dueño: {dueno_info}"
    
    def __len__(self):
        return len(self.__marca) + len(self.__modelo) + len(str(self.__año))
    
class Corazon:
    def latir(self):
        return "El corazón está latiendo"
