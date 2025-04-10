from Empleado import Empleado
from datetime import datetime

class PlantillaEmpleados:
    def __init__(self):
        self.empleados = []

    def meter_empleados(self, empleado: Empleado):
        self.empleados.append(empleado)

    def __str__(self) -> str:
        empleados_str = ""
        for empleado in self.empleados:
            empleados_str += f"{empleado.nombre} - DNI: {empleado.dni}\n"
        return empleados_str

    def empleado_del_año(self, año: int) -> Empleado:
        for empleado in self.empleados:
            pass
    
    def proponer_despidos(self) -> list:
        pass

    def despedir(self, dnis: str):
        for empleado in self.empleados:
            for dni in dnis:
                if empleado.dni == dni:
                    self.empleados.remove(empleado)