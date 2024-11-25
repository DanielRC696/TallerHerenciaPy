#3. Sistema de figuras 3D
"""
Diseña un programa que permita trabajar con figuras tridimensionales.

1. Define una clase base llamada Figura3D que tenga el método calcular_volumen(), el cual inicialmente imprime "Método no implementado".

2. Crea dos clases hijas:

o Cubo:

§ Añade el atributo lado.

§ Implementa el método calcular_volumen() usando la fórmula lado3.

o Esfera:

§ Añade el atributo radio.

§ Implementa el método calcular_volumen() usando la fórmula

"""

class Figura3D:
    def calcular_volumen(self):
        print("Método no implementado.")


class Cubo(Figura3D):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        return self.lado ** 3


class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        import math
        return (4 / 3) * math.pi * (self.radio ** 3)


# Crear objetos
cubo1 = Cubo(3)
esfera1 = Esfera(5)

print(f"Volumen del cubo: {cubo1.calcular_volumen():.2f}")
print(f"Volumen de la esfera: {esfera1.calcular_volumen():.2f}")
