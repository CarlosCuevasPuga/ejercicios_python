from ConsolaPortatil import ConsolaPortatil
from datetime import datetime

consolas_portatiles = [
    ConsolaPortatil("Game Boy", "Nintendo", datetime(1989, 4, 21), ["Gris", "Negro"], False, 30),
    ConsolaPortatil("PSP", "Sony", datetime(2004, 12, 12), ["Negro", "Plata"], False, 6),
    ConsolaPortatil("Nintendo Switch", "Nintendo", datetime(2017, 3, 3), ["Rojo", "Azul"], False, 9),
    ConsolaPortatil("Nintendo DS", "Nintendo", datetime(2004, 11, 21), ["Negro", "Blanco"], False, 10),
    ConsolaPortatil("PS Vita", "Sony", datetime(2011, 12, 17), ["Negro", "Blanco"], False, 6),
    ConsolaPortatil("Neo Geo Pocket", "SNK", datetime(1998, 10, 28), ["Negro", "Blanco"], False, 10),
    ConsolaPortatil("Atari Lynx", "Atari", datetime(1989, 9, 1), ["Negro", "Azul"], False, 5),
    ConsolaPortatil("Gizmondo", "Tiger Telematics", datetime(2005, 3, 10), ["Negro", "Naranja"], True, 5),
    ConsolaPortatil("N-Gage", "Nokia", datetime(2003, 10, 7), ["Negro", "Blanco"], False, 3),
    ConsolaPortatil("Steam Deck", "Valve", datetime(2022, 2, 25), ["Negro"], False, 7)
]

for consola in consolas_portatiles:
    print(consola)

print("-" * 100)

print(consolas_portatiles[0] == consolas_portatiles[2])
print(consolas_portatiles[0] > consolas_portatiles[2])
print(consolas_portatiles[0] > consolas_portatiles[3])
print(consolas_portatiles[0] < consolas_portatiles[2])
print(consolas_portatiles[0] < consolas_portatiles[3])
print(consolas_portatiles[0] >= consolas_portatiles[2])
print(consolas_portatiles[0] >= consolas_portatiles[3])
print(consolas_portatiles[0] <= consolas_portatiles[2])
print(consolas_portatiles[0] <= consolas_portatiles[3])