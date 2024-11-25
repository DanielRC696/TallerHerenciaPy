
# 1. Sistema de biblioteca
"""
Diseña un programa que permita gestionar los materiales de una biblioteca. Sigue estas indicaciones:

1. Crea una clase base llamada MaterialBiblioteca con los siguientes atributos:

o titulo: el título del material.

o autor: el nombre del autor.

o codigo: un código único para identificar el material.

o disponible: un indicador (verdadero/falso) que indique si el material está disponible para préstamo (por defecto True).

2. Implementa los métodos:

o prestar(): cambia el estado de disponible a False si el material está disponible.

o devolver(): cambia el estado de disponible a True.

o mostrar_info(): imprime los detalles del material.

3. A partir de esta clase, crea tres clases hijas:

o Libro: añade los atributos numero_paginas y genero.

o Revista: añade los atributos numero_edicion y fecha_publicacion"""

class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"'{self.titulo}' ha sido prestado.")
        else:
            print(f"'{self.titulo}' no está disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"'{self.titulo}' ha sido devuelto.")
        else:
            print(f"'{self.titulo}' ya estaba disponible.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}, Estado: {estado}")


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_paginas, genero, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_paginas = numero_paginas
        self.genero = genero

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Género: {self.genero}, Páginas: {self.numero_paginas}")


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_edicion, fecha_publicacion, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Edición: {self.numero_edicion}, Publicación: {self.fecha_publicacion}")


# Crear objetos 
libro1 = Libro("La culpa es de la Vaca", "Juan Contreras", "L001", 96, "Ficción")
revista1 = Revista("National Geographic", "Varios", "R001", 202, "Noviembre 2024")

libro1.mostrar_info()
libro1.prestar()
libro1.devolver()

revista1.mostrar_info()
