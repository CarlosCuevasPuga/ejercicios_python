from EjemplarVideojuego import EjemplarVideojuego
from Videojuego import Videojuego
from datetime import datetime


ejemplares = [
    EjemplarVideojuego("The Legend of Zelda", datetime(1986, 2, 21), 9.5, ["Aventura", "Acción"], 1, 1),
    EjemplarVideojuego("Super Mario Bros", datetime(1985, 9, 13), 9.8, ["Plataformas"], 2, 2),
    EjemplarVideojuego("Final Fantasy VII", datetime(1997, 1, 31), 9.7, ["RPG"], 3, 0),
]

ejemplar1 = EjemplarVideojuego("The Legend of Zelda", datetime(1986, 2, 21), 9.5, ["Aventura", "Acción"], 1, 1)
ejemplar2 = EjemplarVideojuego("Super Mario Bros", datetime(1985, 9, 13), 9.8, ["Plataformas"], 2, 2)
ejemplar3 = EjemplarVideojuego("Final Fantasy VII", datetime(1997, 1, 31), 9.7, ["RPG"], 3, 0)

for ejemplar in ejemplares:
    print(ejemplar)

print("--------------------")

print(ejemplar1 > ejemplar2)
print(ejemplar1 < ejemplar2)
print(ejemplar1 == ejemplar2)