from Persona import Persona
from datetime import datetime

class Empleado(Persona):

    def __init__(self, nombre: str, dni: str, fecha_nacimiento: datetime, casado: bool, divorciado: bool, sueldo: float, fecha_alta: datetime, empleado_del_mes: list):
        super().__init__(nombre, dni, fecha_nacimiento, casado, divorciado)

        self.sueldo = sueldo

        if fecha_alta <= datetime.now():
            self.fecha_alta = fecha_alta
        else:
            self.fecha_alta = datetime.now()

        if len(empleado_del_mes) > 0:
            self.empleado_del_mes = empleado_del_mes

    def __str__(self) -> str:
        return super().__str__() + (
            f"Sueldo: {self.sueldo} €, fecha alta: {self.fecha_alta}, numero de veces empleado del mes: {self.n_veces_empleado_mes()}"
        )

    def __gt__(self, other) -> bool:
        if isinstance(other, Empleado):
            return self.sueldo > other.sueldo
        else:
            return False

    def __ge__(self, other) -> bool:
        if isinstance(other, Empleado):
            return self.sueldo >= other.sueldo
        else:
            return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Empleado):
            return self.sueldo < other.sueldo
        else:
            return False

    def __le__(self, other) -> bool:
        if isinstance(other, Empleado):
            return self.sueldo <= other.sueldo
        else:
            return False

    def n_veces_empleado_mes(self) -> int:
        return len(self.empleado_del_mes)

    def ultima_vez_empleado_mes(self) -> datetime:
        pass