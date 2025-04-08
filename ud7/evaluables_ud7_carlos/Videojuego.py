from datetime import datetime

class Videojuego:
    def __init__(self, nombre: set, fecha_salida: datetime, puntuacion: float, generos: list):
        self.nombre = nombre
        self.fecha_salida = fecha_salida
        
        if puntuacion < 0 or puntuacion > 10:
            self.puntuacion = 0
        else:
            self.puntuacion = puntuacion
        
        self.generos = generos

    def __str__(self) -> str:
        return(
            f"Nombre: {self.nombre},"
            f"Fecha de salida: {self.fecha_salida},"
            f"Puntuación: {self.puntuacion},"
            f"Generos: {self.generos}"
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, Videojuego):
            return self.nombre == other.nombre and self.fecha_salida == other.fecha_salida
        else:
            return False

    def __gt__(self, other) -> bool:
        if isinstance(other, Videojuego):
            return self.puntuacion > other.puntuacion
        return False

    def __ge__(self, other) -> bool:
        if isinstance(other, Videojuego):
            return self.puntuacion >= other.puntuacion
        else:
            return False


    def __lt__(self, other) -> bool:
        if isinstance(other, Videojuego):
            return self.puntuacion < other.puntuacion
        else:
            return False

    def __le__(self, other) -> bool:
        if isinstance(other, Videojuego):
            return self.puntuacion <= other.puntuacion
        else:
            return False

    def es_del_genero(self, genero: str) -> bool:
        return genero in self.generos