#4. Sistema de Vehículos de Carreras
"""
Construye un sistema para gestionar vehículos de carreras.

1. Crea una clase base llamada VehiculoCarreras con los siguientes atributos:

o marca: la marca del vehículo.

o modelo: el modelo del vehículo.

o velocidad_maxima: la velocidad máxima del vehículo (en km/h).

2. Implementa el método mostrar_info(), que imprime los detalles básicos del vehículo.

3. Crea tres clases hijas:

o CocheF1: añade el atributo tipo_neumaticos (tipo de llantas utilizadas).

o MotoGP: añade el atributo tipo_carenado (tipo de estructura aerodinámica).
"""

class VehiculoCarreras:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad Máxima: {self.velocidad_maxima} km/h")


class CocheF1(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Neumáticos: {self.tipo_neumaticos}")


class MotoGP(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Carenado: {self.tipo_carenado}")


# Crear objetos
coche1 = CocheF1("Ferrari", "SF23", 350, "Lluvia")
moto1 = MotoGP("Yamaha", "YZR-M1", 300, "Aerodinámico")

coche1.mostrar_info()
moto1.mostrar_info()
