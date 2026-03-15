class Transporte:
    """Clase base para representar un medio de transporte.
    Atributos:
        tipo (str): El tipo de transporte (e.g., bicicleta, cuadraciclo, patineta).
        capacidad (int): La capacidad de personas que puede transportar.    
    Métodos:
        __str__: Devuelve una representación en cadena del transporte.
    """
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El tipo no puede estar vacío.")
        self._tipo = valor.strip()

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if valor <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")
        self._capacidad = valor

    def __str__(self):
        return f"{self.__class__.__name__} | Tipo: {self.tipo} | Capacidad: {self.capacidad}"


class Bicicleta(Transporte):
    def __init__(self, tipo, capacidad, marca):
        super().__init__(tipo, capacidad)
        self.marca = marca

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        if not valor or not valor.strip():
            raise ValueError("La marca no puede estar vacía.")
        self._marca = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Marca: {self.marca}"


class Cuadraciclo(Transporte):
    def __init__(self, tipo, capacidad, modelo):
        super().__init__(tipo, capacidad)
        self.modelo = modelo

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El modelo no puede estar vacío.")
        self._modelo = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Modelo: {self.modelo}"


class Patineta(Transporte):
    def __init__(self, tipo, capacidad, color):
        super().__init__(tipo, capacidad)
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El color no puede estar vacío.")
        self._color = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Color: {self.color}"
