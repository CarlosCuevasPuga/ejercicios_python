from Jugador import Jugador
from datetime import datetime

atletico_madrid = [
   Jugador("Jan Oblak", 13, "Portero", 300, 0, 3, 10, 1, datetime(1993, 1, 7), datetime(2014, 7, 16), True),
   Jugador("José María Giménez", 2, "Defensa", 250, 10, 2, 40, 2, datetime(1995, 1, 20), datetime(2013, 4, 1), True),
   Jugador("Stefan Savic", 15, "Defensa", 230, 5, 0, 50, 3, datetime(1991, 1, 8), datetime(2015, 7, 20), True),
   Jugador("Mario Hermoso", 22, "Defensa", 150, 0, 0, 30, 1, datetime(1995, 6, 18), datetime(2019, 7, 18), True),
   Jugador("Nahuel Molina", 16, "Defensa", 50, 3, 0, 10, 0, datetime(1998, 4, 6), datetime(2022, 7, 28), True),
   Jugador("Koke Resurrección", 6, "Centrocampista", 550, 50, 1, 80, 2, datetime(1992, 1, 8), datetime(2009, 9, 19), True),
   Jugador("Marcos Llorente", 14, "Centrocampista", 200, 30, 0, 40, 1, datetime(1995, 1, 30), datetime(2019, 7, 1), True),
   Jugador("Rodrigo De Paul", 5, "Centrocampista", 70, 10, 0, 20, 0, datetime(1994, 5, 24), datetime(2021, 7, 12), True),
   Jugador("Saúl Ñíguez", 8, "Centrocampista", 350, 40, 0, 60, 3, datetime(1994, 11, 21), datetime(2012, 3, 8), True),
   Jugador("Antoine Griezmann", 7, "Delantero", 450, 180, 5, 40, 2, datetime(1991, 3, 21), datetime(2014, 7, 28), True),
   Jugador("Álvaro Morata", 9, "Delantero", 300, 110, 4, 50, 1, datetime(1992, 10, 23), datetime(2020, 7, 1), True),
   Jugador("Ivo Grbić",1,"Portero",20,0,0,1,0,datetime(1996,1,18),datetime(2020,8,20), False),
   Jugador("Reinildo Mandava",23,"Defensa",60,2,0,15,1,datetime(1994,1,21),datetime(2022,1,31), False),
   Jugador("Pablo Barrios",24,"Centrocampista",15,0,0,5,0,datetime(2003,6,15),datetime(2022,12,1), False),
   Jugador("Memphis Depay",19,"Delantero",30,10,0,6,1,datetime(1994,2,13),datetime(2023,1,20), False)
]

def f2a(jugadores: list) -> Jugador:
    max_jugador_mas_partidos_jugados = max([jugador.partidos_jugados for jugador in jugadores])
    for jugador in jugadores:
        if jugador.partidos_jugados == max_jugador_mas_partidos_jugados:
            return jugador.nombre

def f2b(jugadores: list) -> Jugador:
    max_radio_goles = max([jugador.ratio_goles() for jugador in jugadores])
    for jugador in jugadores:
        if jugador.ratio_goles() == max_radio_goles:
            return jugador.nombre

def f2c(jugadores: list) -> Jugador:
    max_gol_defensas = max([jugador.goles for jugador in jugadores if jugador.posicion == "Defensa"])
    for jugador in jugadores:
        if jugador.goles == max_gol_defensas and jugador.posicion == "Defensa":
            return jugador.nombre

def f2d(jugadores: list) -> list:
    max_radio_goleador_defensas = max([jugador.ratio_goles() for jugador in jugadores if jugador.posicion == "Defensa"])
    max_radio_goleador_centrocampistas = max([jugador.ratio_goles() for jugador in jugadores if jugador.posicion == "Centrocampista"])
    max_radio_goleador_delanteros = max([jugador.ratio_goles() for jugador in jugadores if jugador.posicion == "Delantero"])
    defensa_centro_delant = []
    for jugador in jugadores:
        if jugador.ratio_goles() == max_radio_goleador_defensas and jugador.posicion == "Defensa":
            defensa_centro_delant.append(jugador.nombre)
        elif jugador.ratio_goles() == max_radio_goleador_centrocampistas and jugador.posicion == "Centrocampista":
            defensa_centro_delant.append(jugador.nombre)
        elif jugador.ratio_goles() == max_radio_goleador_delanteros and jugador.posicion == "Delantero":
            defensa_centro_delant.append(jugador.nombre)
    return defensa_centro_delant

def f2e(jugadores: list) -> list:
    jugadores_menor_28 = [jugador.nombre for jugador in jugadores]
    return jugadores_menor_28

def f2f(jugadores: list) -> list:
    no_porteros_sin_goles = [jugador.nombre for jugador in jugadores if jugador.goles == 0 and not jugador.posicion == "Portero"]
    return no_porteros_sin_goles

def f2g(jugadores: list) -> list:
    jugadores_en_club_antes_2015 = [jugador.nombre for jugador in jugadores if jugador.fecha_alta.year < 2015]
    return jugadores_en_club_antes_2015

def f2h(jugadores: list) -> list:
    delantero_menos_goles = min([jugador.goles for jugador in jugadores if jugador.posicion == "Delantero"])
    centrocampistas_mas_goles_delantero = []
    for jugador in jugadores:
        if jugador.goles > delantero_menos_goles and jugador.posicion == "Centrocampista":
            centrocampistas_mas_goles_delantero.append(jugador.nombre)
    return centrocampistas_mas_goles_delantero

jugador_mas_partidos = f2a(atletico_madrid)
jugador_mejor_ratio_goleador = f2b(atletico_madrid)
defensa_con_mas_goles = f2c(atletico_madrid)
goleadores_defensa_centro_delant = f2d(atletico_madrid)
jugadores_igual_menor_28 = f2e(atletico_madrid)
no_porteros_sin_goles = f2f(atletico_madrid)
jugadores_antes_2015 = f2g(atletico_madrid)
centros_mas_goles_delant = f2h(atletico_madrid)

print(f"2a. Jugador con más partidos: {jugador_mas_partidos}")
print("\n-----------------\n")
print(f"2.b Jugador con mejor ratio goleador: {jugador_mejor_ratio_goleador}")
print("\n-----------------\n")
print(f"2.c Defensa con más goles: {defensa_con_mas_goles}")
print("\n-----------------\n")
print("2.d Los jugadores, por posición, con mejor ratio goleador son:")
print(f"Defensa: {goleadores_defensa_centro_delant[0]}")
print(f"Centrocampista: {goleadores_defensa_centro_delant[1]}")
print(f"Delantero: {goleadores_defensa_centro_delant[2]}")
print("\n-----------------\n")
print(f"Los jugadores con 28 o menos años son: {jugadores_igual_menor_28}")
print("\n-----------------\n")
print(f"Los jugadores que nunca han metido gol y que no son porteros son: {no_porteros_sin_goles}")
print("\n-----------------\n")
print(f"Los jugadores que llevan en el equipo desde antes de 2015 son: {jugadores_antes_2015}")
print("\n-----------------\n")
print(f"Los Centrocampistas que han marcado más goles que algún delantero son: {centros_mas_goles_delant}")