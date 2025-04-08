from Videojuego import Videojuego
from datetime import datetime


videojuegos = [
    Videojuego("The Legend of Zelda: Breath of the Wild", datetime(2017, 3, 3), 11, ["Aventura", "Acción"]),
    Videojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Acción"]),
    Videojuego("Dark Souls", datetime(2011, 6, 24), 9.0, ["RPG", "Acción"]),
    Videojuego("Celeste", datetime(2018, 1, 25), 9.3, ["Plataformas", "Indie"]),
    Videojuego("Hollow Knight", datetime(2017, 2, 24), 9.4, ["Aventura", "Metroidvania"]),
]

videojuego1 = Videojuego("The Legend of Zelda: Breath of the Wild", datetime(2017, 3, 3), 11, ["Aventura", "Acción"]),
videojuego2 = Videojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Acción"]),
videojuego3 = Videojuego("Dark Souls", datetime(2011, 6, 24), 9.0, ["RPG", "Acción"]),
videojuego4 = Videojuego("Celeste", datetime(2018, 1, 25), 9.3, ["Plataformas", "Indie"]),
videojuego5 = Videojuego("Hollow Knight", datetime(2017, 2, 24), 9.4, ["Aventura", "Metroidvania"]),

for videojuego in videojuegos:
    print(videojuego.es_del_genero("RPG"))

print("--------------------")

print(videojuego1 < videojuego2)
print(videojuego3 > videojuego4)
print(videojuego5 <= videojuego1)
print(videojuego2 >= videojuego3)
print(videojuego1 == videojuego1)
