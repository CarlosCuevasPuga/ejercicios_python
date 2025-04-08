from Videojuego import Videojuego
from datetime import datetime

class EjemplarVideojuego(Videojuego):
    def __init__(self, nombre: set, fecha_salida: datetime, puntuacion: float, generos: list, id: int, estado: int):
        super().__init__(nombre, fecha_salida, puntuacion, generos)

        self.id = id
        self.estado = estado

    def __str__(self) -> str:
        return super().__str__() + (
            f"ID: {self.id},"
            f"Estado: {self.estado_str()}"
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, EjemplarVideojuego):
            return self.id == other.id
        else:
            return False

    def __gt__(self, other) -> bool:
        if isinstance(other, EjemplarVideojuego):
            return self.estado < other.estado
        else:
            return False
    
    def __ge__(self, other) -> bool:
        if isinstance(other, EjemplarVideojuego):
            return self.estado <= other.estado
        else:
            return False

    def __lt__(self, other) -> bool:
        if isinstance(other, EjemplarVideojuego):
            return self.estado > other.estado
        else:
            return False

    def __le__(self, other) -> bool:
        if isinstance(other, EjemplarVideojuego):
            return self.estado >= other.estado
        else:
            return False

    def estado_str(self) -> str:
        estado = "Desconocido"
        
        if self.estado == 1:
            estado = "Nuevo"
        elif self.estado == 2:
            estado = "Como nuevo"
        elif self.estado == 3:
            estado = " ligeros desperfectos"
        elif self.estado == 4: 
            estado = "desperfectos grandes"
        elif self.estado == 5:
            estado = "sin caja y/o manual"

        return estado