import random

def emparejar_listas(equipos1: list, equipos2: list):
    equipos1_copia = equipos1.copy()
    equipos2_copia = equipos2.copy()
    emparejamientos = []

    while len(equipos1_copia) > 0:

        index1 = random.randint(0, len(equipos1_copia) - 1)
        equipo1 = equipos1_copia.pop(index1)

        index2 = random.randint(0, len(equipos2_copia) - 1)
        equipo2 = equipos2_copia.pop(index2)
        
        emparejamientos.append((equipo1, equipo2))
    for nombre in emparejamientos:
        print(f"{nombre[0]} vs {nombre[1]}")
    

equipos1 = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Bilbao"]
equipos2 = ["Real Sociedad", "Betis", "Granada", "Valencia"]

emparejar_listas(equipos1, equipos2)