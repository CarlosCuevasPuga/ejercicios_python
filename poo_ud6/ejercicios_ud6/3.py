from videojuego import Videojuego

juegos = [
    Videojuego(
    "The Witcher 3",
    ["RPG","Acción","Aventura"],
    "19/05/2015",
    9.7,
    18,
    39.99,
    50
),

    Videojuego(
    "Grand Thef Auto V",
    ["Acción","Mundo Abierto"],
    "17/09/2013",
    9.5,
    18,
    29.99,
    95
),

    Videojuego(
    "The Legend of Zelda: Breath of the Wild",
    ["Aventura","Mundo Abierto"],
    "3/03/2017",
    10.0,
    12,
    59.99,
    13.4
),

    Videojuego(
    "Minecraft",
    ["Supervivencia","Sandbox"],
    "18/11/2011",
    9.0,
    7,
    26.95,
    1.2
),

    Videojuego(
    "Red Dead Redemption 2",
    ["Acción","Mundo Abierto"],
    "26/10/2018",
    9.8,
    18,
    59.99,
    150
),

    Videojuego(
    "God of War (2018)",
    ["Acción","Aventura"],
    "20/04/2018",
    9.6,
    18,
    49.99,
    45
),

    Videojuego(
    "Dark Souls III",
    ["RPG","Acción"],
    "12/04/2016",
    9.3,
    16,
    39.99,
    25
),

    Videojuego(
    "Animal Crossing: New Horizons",
    ["Simulación","Social"],
    "20/03/2020",
    9.1,
    3,
    49.99,
    10.2
),

    Videojuego(
    "Cyberpunk 2077",
    ["RPG","Mundo Abierto"],
    "10/12/2020",
    8.5,
    18,
    59.99,
    70
),

    Videojuego(
    "Super Mario Odyssey",
    ["Plataformas","Aventura"],
    "27/10/2017",
    9.8,
    7,
    49.99,
    5.6
)

]

for juego in juegos:
    print(f"{juego.nombre}: {juego.precio_final(0.21,0)}€")