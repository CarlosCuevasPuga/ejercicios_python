from ConsolaSobreMesa import ConsolaSobreMesa
from datetime import datetime

consolas_sobremesa = [
    ConsolaSobreMesa("PlayStation 5", "Sony", datetime(2020, 11, 12), ["Blanco", "Negro"], False, 2),
    ConsolaSobreMesa("Xbox Series X", "Microsoft", datetime(2020, 11, 10), ["Negro"], False, 1),
    ConsolaSobreMesa("Nintendo Switch", "Nintendo", datetime(2017, 3, 3), ["Rojo", "Azul"], False, 2),
    ConsolaSobreMesa("Sega Genesis Mini", "Sega", datetime(2019, 9, 19), ["Negro", "Rojo"], True, 1),
    ConsolaSobreMesa("Atari VCS", "Atari", datetime(2020, 6, 15), ["Negro"], False, 1),
    ConsolaSobreMesa("PlayStation 4 Pro", "Sony", datetime(2016, 11, 10), ["Negro"], False, 1),
    ConsolaSobreMesa("Xbox One X", "Microsoft", datetime(2017, 11, 7), ["Negro"], False, 1),
    ConsolaSobreMesa("Nintendo Classic Mini", "Nintendo", datetime(2016, 11, 11), ["Gris"], True, 1),
    ConsolaSobreMesa("Neo Geo Mini", "SNK", datetime(2018, 7, 24), ["Negro", "Rojo"], True, 1),
    ConsolaSobreMesa("PlayStation Classic", "Sony", datetime(2018, 12, 3), ["Gris"], True, 1)
]

for consola in consolas_sobremesa:
    print(consola)

print("-" * 140)

print(consolas_sobremesa[0] == consolas_sobremesa[2])
print(consolas_sobremesa[0] > consolas_sobremesa[2])
print(consolas_sobremesa[0] > consolas_sobremesa[3])
print(consolas_sobremesa[0] < consolas_sobremesa[2])
print(consolas_sobremesa[0] < consolas_sobremesa[3])
print(consolas_sobremesa[0] >= consolas_sobremesa[2])
print(consolas_sobremesa[0] >= consolas_sobremesa[3])
print(consolas_sobremesa[0] <= consolas_sobremesa[2])
print(consolas_sobremesa[0] <= consolas_sobremesa[3])