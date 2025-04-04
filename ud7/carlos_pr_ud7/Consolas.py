from datetime import datetime

class Consolas:
    def __init__(self, nombre: str, desarrolladores: str, direccion_mac: str, fecha_salida: datetime, colores: list):
        self.nombre = nombre
        self.desarrolladores = desarrolladores
        self.direccion_mac = direccion_mac
        if fecha_salida < datetime.now():
            self.fecha_salida = fecha_salida
        else:
            self.fecha_salida = datetime.now()
        self.colores = colores

    def __eq__(self, other) -> bool:
        if isinstance(other, Consolas):
            return self.direccion_mac == other.direccion_mac
        return False

    def __lt__(self, other) -> bool:
        return self.fecha_salida < other.fecha_salida

    def __le__(self, other) -> bool:
        return self.fecha_salida <= other.fecha_salida

    def __gt__(self, other) -> bool:
        return self.fecha_salida > other.fecha_salida

    def __ge__(self, other) -> bool:
        return self.fecha_salida >= other.fecha_salida