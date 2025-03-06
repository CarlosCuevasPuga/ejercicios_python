equipos = [
    "Real Madrid",
    "Atlético de Madrid",
    "FC Barcelona",
    "Athletic Club",
    "Villarreal CF",
    "Rayo Vallecano",
    "Real Sociedad",
    "Girona FC",
    "CA Osasuna",
    "RCD Mallorca",
    "Real Betis Balompié",
    "RC Celta de Vigo",
    "Sevilla FC",
    "Getafe CF",
    "UD Las Palmas",
    "RCD Espanyol",
    "CD Leganés",
    "Valencia CF",
    "Deportivo Alavés",
    "Real Valladolid CF"
]

while True:
    try:
        nombre_equipo = input("Introduce el nombre del equipo: ")
    except Exception as error:
        print(f"[ERROR] Ha introducido un equipo no valido {error}")
    else:
        posicion = equipos.index(nombre_equipo)
        print(f"El equipo {nombre_equipo} esta en la posición: {posicion + 1}")
