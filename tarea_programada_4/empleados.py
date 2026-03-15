class Empleados:
    """
    Clase base para representar un empleado.
    Atributos:
        nombre (str): El nombre del empleado.
        edad (int): La edad del empleado en años.
    Métodos:
        __str__: Devuelve una representación en cadena del empleado.
    """
    def __init__(self, nombre, edad):
        self.nombre = nombre
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
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = valor

    def __str__(self):
        return f"{self.__class__.__name__} | Nombre: {self.nombre} | Edad: {self.edad}"


class Administrador(Empleados):
    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.departamento = departamento

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El departamento no puede estar vacío.")
        self._departamento = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Departamento: {self.departamento}"


class Guardian(Empleados):
    def __init__(self, nombre, edad, turno):
        super().__init__(nombre, edad)
        self.turno = turno

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El turno no puede estar vacío.")
        self._turno = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Turno: {self.turno}"


class Conserje(Empleados):
    def __init__(self, nombre, edad, area):
        super().__init__(nombre, edad)
        self.area = area

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El área no puede estar vacía.")
        self._area = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Área: {self.area}"


class Veterinario(Empleados):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not valor or not valor.strip():
            raise ValueError("La especialidad no puede estar vacía.")
        self._especialidad = valor.strip()

    def __str__(self):
        return f"{super().__str__()} | Especialidad: {self.especialidad}"
