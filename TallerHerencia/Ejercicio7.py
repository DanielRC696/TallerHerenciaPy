#7. Sistema de transporte público
"""
Crea un sistema para registrar diferentes tipos de transporte público:

1. Define una clase base llamada TransportePublico con los atributos:

o tipo: el tipo de transporte (e.g., autobús, tren).

o capacidad: el número máximo de pasajeros.

2. Implementa el método mostrar_info(), que imprime los detalles básicos del transporte.

3. Crea tres clases hijas:

o Autobus: añade el atributo ruta (número o nombre de la ruta).

o Tren: añade el atributo numero_vagones (cantidad de vagones)
"""

class TransportePublico:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar_info(self):
        print(f"Tipo de Transporte: {self.tipo}, Capacidad: {self.capacidad} pasajeros")


class Autobus(TransportePublico):
    def __init__(self, tipo, capacidad, ruta):
        super().__init__(tipo, capacidad)
        self.ruta = ruta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Ruta: {self.ruta}")


class Tren(TransportePublico):
    def __init__(self, tipo, capacidad, numero_vagones):
        super().__init__(tipo, capacidad)
        self.numero_vagones = numero_vagones

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Vagones: {self.numero_vagones}")


# Crear objetos
autobus1 = Autobus("Bus", 50, "Ruta 2 Itagui")
tren1 = Tren("Tren", 200, 10)

autobus1.mostrar_info()
tren1.mostrar_info()
