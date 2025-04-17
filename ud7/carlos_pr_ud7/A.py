from Consola import Consola
from datetime import datetime

consolas = [
    Consola("PlayStation 5", ["Sony"], datetime(2020, 11, 12)),
    Consola("Xbox Series X", ["Microsoft"], datetime(2020, 11, 10)),
    Consola("Nintendo Switch", ["Nintendo"], datetime(2017, 3, 3)),
    Consola("PlayStation 4", ["Sony"], datetime(2013, 11, 15)),
    Consola("Xbox One", ["Microsoft"], datetime(2013, 11, 22)),
    Consola("Nintendo 3DS", ["Nintendo"], datetime(2011, 2, 26)),
    Consola("Sega Genesis", ["Sega"], datetime(1988, 8, 14)),
    Consola("Super Nintendo", ["Nintendo"], datetime(1990, 8, 23)),
    Consola("Xbox 360", ["Microsoft"], datetime(2005, 11, 22)),
    Consola("PlayStation Portable", ["Sony"], datetime(2004, 12, 12)),
    Consola("PlayBox super colab", ["Sony", "Microsoft"], datetime(2020, 11, 12)) #Ejemplo de prueba,
]

for consola in consolas:
    print(consola)

print("-" * 100)

print(consolas[0] == consolas[2])
print(consolas[0] > consolas[2])
print(consolas[0] > consolas[3])
print(consolas[0] < consolas[2])
print(consolas[0] < consolas[3])
print(consolas[0] >= consolas[2])
print(consolas[0] >= consolas[3])
print(consolas[0] <= consolas[2])
print(consolas[0] <= consolas[3])
consolas_mas_1_desarr = [consola for consola in consolas if consola.mas_de_1_desarrollador() == True]
for consola in consolas_mas_1_desarr:
    print(consola)