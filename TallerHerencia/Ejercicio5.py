#5. Sistema de Mascotas
"""
Crea un programa que registre diferentes tipos de mascotas:

1. Define una clase base llamada Mascota con los atributos:

o nombre: el nombre de la mascota.

o edad: la edad de la mascota (en años).

o especie: el tipo de animal (e.g., perro, gato).

2. Implementa el método mostrar_info(), que imprime los detalles básicos de la mascota.

3. Crea tres clases hijas:

o Perro: añade el atributo raza y el método ladrar(), que imprime "Guau, guau".

o Gato: añade el atributo color y el método maullar(), que imprime "Miau".
"""
class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}")


class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Perro")
        self.raza = raza

    def ladrar(self):
        print("Guau, guau")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raza: {self.raza}")


class Gato(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad, "Gato")
        self.color = color

    def maullar(self):
        print("Miau")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Color: {self.color}")


# Crear objetos
perro1 = Perro("Fido", 3, "Golden Retriever")
gato1 = Gato("Michi", 2, "Negro")

perro1.mostrar_info()
perro1.ladrar()

gato1.mostrar_info()
gato1.maullar()
