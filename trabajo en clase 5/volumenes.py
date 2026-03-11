from abc import ABC, abstractmethod
import math

# Clase abstracta
class Figura(ABC):

    @abstractmethod
    def volumen(self):
        pass


# Cubo
class Cubo(Figura):
    def __init__(self, lado):
        self.lado = lado

    def volumen(self):
        return self.lado ** 3


# Paralelepípedo
class Paralelepipedo(Figura):
    def __init__(self, largo, ancho, altura):
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def volumen(self):
        return self.largo * self.ancho * self.altura


# Cilindro
class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return math.pi * (self.radio ** 2) * self.altura


# Esfera
class Esfera(Figura):
    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)


# Cono
class Cono(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return (1/3) * math.pi * (self.radio ** 2) * self.altura



def imprimir_volumen(figura: Figura):
    print("Volumen:", figura.volumen())


# MAIN
def main():
    # Objetos
    cubo = Cubo(3)
    paralelepipedo = Paralelepipedo(3, 4, 5)
    cilindro = Cilindro(2, 5)
    esfera = Esfera(3)
    cono = Cono(2, 6)

    # Imprimir volúmenes
    imprimir_volumen(cubo)
    imprimir_volumen(paralelepipedo)
    imprimir_volumen(cilindro)
    imprimir_volumen(esfera)
    imprimir_volumen(cono)

if __name__ == "__main__":
    main()