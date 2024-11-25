# 2. Sistema de empleados de un hospital
"""
Crea un sistema para registrar y describir empleados de un hospital.

1. Diseña una clase base llamada EmpleadoHospital con los atributos:

o nombre: el nombre del empleado.

o id: un identificador único para cada empleado.

o departamento: el área donde trabaja (e.g., pediatría, urgencias).

o salario_base: el salario inicial del empleado.

2. Implementa el método mostrar_info(), que imprime los detalles del empleado.

3. Crea tres clases hijas:

o Medico: añade los atributos especialidad (e.g., cardiología) y num_pacientes (número de pacientes atendidos).

o Enfermero: añade los atributos turno (mañana o noche) y planta (el número de la planta en el hospital).
"""

class EmpleadoHospital:
    def __init__(self, nombre, id, departamento, salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario_base = salario_base

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, ID: {self.id}, Departamento: {self.departamento}, Salario: {self.salario_base:.2f}")


class Medico(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        super().__init__(nombre, id, departamento, salario_base)
        self.especialidad = especialidad
        self.num_pacientes = num_pacientes

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}, Pacientes atendidos: {self.num_pacientes}")


class Enfermero(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, turno, planta):
        super().__init__(nombre, id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Turno: {self.turno}, Planta: {self.planta}")


# Crear objetos
medico1 = Medico("Dr. Smith", "M001", "Cardiología", 8000, "Cardiólogo", 20)
enfermero1 = Enfermero("Carlos", "E001", "Pediatría", 3000, "Noche", 2)

medico1.mostrar_info()
enfermero1.mostrar_info()
