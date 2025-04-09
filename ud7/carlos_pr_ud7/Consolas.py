from datetime import datetime

class Consola:
    def __init__(self, nombre: str, desarrollador: str, fecha_salida: datetime):
        self.nombre = nombre
        self.desarrollador = desarrollador
        
        if fecha_salida < datetime.now():
            self.fecha_salida = fecha_salida
        else:
            self.fecha_salida = datetime.now()

    def __str__(self) -> str:
        return (
            f"Nombre: {self.nombre}, "
            f"Desarrolladores: {self.desarrollador}, "
            f"Fecha de Salida: {self.fecha_salida}"
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, Consola):
            return self.nombre == other.nombre and self.fecha_salida == other.fecha_salida
        return False

    def __lt__(self, other) -> bool:
        return self.fecha_salida > other.fecha_salida

    def __le__(self, other) -> bool:
        return self.fecha_salida >= other.fecha_salida

    def __gt__(self, other) -> bool:
        return self.fecha_salida < other.fecha_salida

    def __ge__(self, other) -> bool:
        return self.fecha_salida <= other.fecha_salida