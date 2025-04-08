from ColeccionVideojuegos import ColeccionVideojuegos
from EjemplarVideojuego import EjemplarVideojuego
from datetime import datetime

videojuegos = [
    EjemplarVideojuego("The Legend of Zelda: Breath of the Wild", datetime(2017, 3, 3), 10, ["Acción", "Aventura", "Mundo Abierto"], 1, 5),
    EjemplarVideojuego("Read Dead Redemption 2", datetime(2018, 10, 26), 9.8, ["Acción", "Aventura", "Mundo Abierto"], 2, 4),
    EjemplarVideojuego("Elden Ring", datetime(2022, 2, 25), 9.7, ["RPG", "Acción", "Mundo Abierto"], 3, 5),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "Mundo Abierto"], 4, 3),
    EjemplarVideojuego("The Witcher 3: Wild Hunt", datetime(2015, 5, 19), 9.5, ["RPG", "Aventura", "Mundo Abierto"], 5, 1),
]

coleccion = ColeccionVideojuegos()

# Mostrar los juegos (nombre y estado)
for juego in videojuegos:
    coleccion.meter_videojuegos(juego)

print(coleccion)

print("------------------")

#Mostrar los juegos repetidos
coleccion.mostrar_juegos_repetidos()

print("-------------------")

#Eliminado el juego con ID 4
coleccion.eliminar_juego(4)

#Mostrar otra vez los juegos
print(coleccion)