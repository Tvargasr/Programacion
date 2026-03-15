class Animal:
    """Clase base para representar un animal.
    Atributos:
        nombre (str): El nombre del animal.
        especie (str): La especie del animal.
        edad (int): La edad del animal en años.
    
    Métodos:
        __str__: Devuelve una representación en cadena del animal.
    """

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self, valor):
        if not valor or not valor.strip():
            raise ValueError("La especie no puede estar vacía.")
        self._especie = valor.strip()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = valor

    def __str__(self):
        return f"{self.__class__.__name__} | Nombre: {self.nombre} | Especie: {self.especie} | Edad: {self.edad}"


class Mamifero(Animal):
    def __init__(self, nombre, especie, edad, tipo_pelo):
        super().__init__(nombre, especie, edad)
        self.tipo_pelo = tipo_pelo

    @property
    def tipo_pelo(self):
        return self._tipo_pelo

    @tipo_pelo.setter
    def tipo_pelo(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El tipo de pelo no puede estar vacío.")
        self._tipo_pelo = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Tipo de pelo: {self.tipo_pelo}"


class Ave(Animal):
    def __init__(self, nombre, especie, edad, tipo_pluma):
        super().__init__(nombre, especie, edad)
        self.tipo_pluma = tipo_pluma

    @property
    def tipo_pluma(self):
        return self._tipo_pluma

    @tipo_pluma.setter
    def tipo_pluma(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El tipo de pluma no puede estar vacío.")
        self._tipo_pluma = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Tipo de pluma: {self.tipo_pluma}"


class Reptil(Animal):
    def __init__(self, nombre, especie, edad, tipo_escama):
        super().__init__(nombre, especie, edad)
        self.tipo_escama = tipo_escama

    @property
    def tipo_escama(self):
        return self._tipo_escama

    @tipo_escama.setter
    def tipo_escama(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El tipo de escama no puede estar vacío.")
        self._tipo_escama = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Tipo de escama: {self.tipo_escama}"


class Pez(Animal):
    def __init__(self, nombre, especie, edad, tipo_agua):
        super().__init__(nombre, especie, edad)
        self.tipo_agua = tipo_agua

    @property
    def tipo_agua(self):
        return self._tipo_agua

    @tipo_agua.setter
    def tipo_agua(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El tipo de agua no puede estar vacío.")
        self._tipo_agua = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Tipo de agua: {self.tipo_agua}"


class Anfibio(Animal):
    def __init__(self, nombre, especie, edad, tipo_piel):
        super().__init__(nombre, especie, edad)
        self.tipo_piel = tipo_piel

    @property
    def tipo_piel(self):
        return self._tipo_piel

    @tipo_piel.setter
    def tipo_piel(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El tipo de piel no puede estar vacío.")
        self._tipo_piel = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Tipo de piel: {self.tipo_piel}"


class Leon(Mamifero):
    def __init__(self, nombre, edad, tipo_pelo):
        super().__init__(nombre, "León", edad, tipo_pelo)


class Aguila(Ave):
    def __init__(self, nombre, edad, tipo_pluma):
        super().__init__(nombre, "Águila", edad, tipo_pluma)


class Serpiente(Reptil):
    def __init__(self, nombre, edad, tipo_escama):
        super().__init__(nombre, "Serpiente", edad, tipo_escama)


class PezPayaso(Pez):
    def __init__(self, nombre, edad, tipo_agua):
        super().__init__(nombre, "Pez payaso", edad, tipo_agua)


class Rana(Anfibio):
    def __init__(self, nombre, edad, tipo_piel):
        super().__init__(nombre, "Rana", edad, tipo_piel)
