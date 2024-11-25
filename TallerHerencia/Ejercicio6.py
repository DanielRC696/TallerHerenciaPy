#6. Sistema de productos electrónicos
"""
Diseña un programa para gestionar dispositivos electrónicos:

1. Crea una clase base llamada ProductoElectronico con los atributos:

o nombre: el nombre del dispositivo.

o precio: el precio del dispositivo (en dólares).

o marca: la marca del dispositivo.

2. Implementa el método mostrar_info(), que imprime los detalles del producto.

3. Crea tres clases hijas:

o TelefonoMovil: añade el atributo capacidad_bateria (en mAh).

o Laptop: añade el atributo tamano_pantalla (en pulgadas).
"""

class ProductoElectronico:
    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Marca: {self.marca}")


class TelefonoMovil(ProductoElectronico):
    def __init__(self, nombre, precio, marca, capacidad_bateria):
        super().__init__(nombre, precio, marca)
        self.capacidad_bateria = capacidad_bateria

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de Batería: {self.capacidad_bateria} mAh")


class Laptop(ProductoElectronico):
    def __init__(self, nombre, precio, marca, tamano_pantalla):
        super().__init__(nombre, precio, marca)
        self.tamano_pantalla = tamano_pantalla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tamaño de Pantalla: {self.tamano_pantalla} pulgadas")


# Crear objetos
telefono1 = TelefonoMovil("iPhone 14", 999, "Apple", 3200)
laptop1 = Laptop("HP-6978", 1200, "HP", 13.3)

telefono1.mostrar_info()
laptop1.mostrar_info()
