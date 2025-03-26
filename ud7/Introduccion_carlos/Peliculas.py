class Peliculas:
    def __init__(self, nombre: str, cod: str, PEGI: int, duracion: float, generos: list, actores: list, puntuacion: int, num_vistas: int):
        self.nombre = nombre
        self.cod = cod
        self.PEGI = PEGI
        self.duracion = duracion
        self.generos = generos
        self.actores = actores
        self.puntuacion = puntuacion
        self.num_vistas = num_vistas

    def __str__(self) -> str:
        return (
            f"Nombre: {self.nombre}\n"
            f"Codigo: {self.cod}\n"
            f"PEGI: {self.PEGI}\n"
            f"Duracion: {self.duracion} minutos\n"
            f"Generos: {self.generos}\n"
            f"Actores implicados: {self.actores}\n"
            f"Puntuación: {self.puntuacion}\n"
            f"Número de veces vista: {self.num_vistas}"
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, Peliculas):
            return self.cod == other.cod
        return False

    def __lt__(self, other):
        if isinstance(other, Peliculas):
            return self.puntuacion < other.puntuacion
    
    def __gt__(self, other):
        if isinstance(other, Peliculas):
            return self.puntuacion > other.puntuacion

    def pelis_con_pegi_18(self) -> list:
        return [self.nombre for _ in Peliculas if self.PEGI == 18]