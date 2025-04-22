from ConsolaSobreMesa import ConsolaSobreMesa
from datetime import datetime

consolas_sobremesa = [
    ConsolaSobreMesa("PlayStation 5", ["Sony"], datetime(2020, 11, 12), ["Blanco", "Negro"], False, 825, 4),
    ConsolaSobreMesa("Xbox Series X", ["Microsoft"], datetime(2020, 11, 10), ["Negro"], False, 1000, 3),
    ConsolaSobreMesa("Nintendo Switch", ["Nintendo"], datetime(2017, 3, 3), ["Rojo", "Azul"], False, 32, 2),
    ConsolaSobreMesa("Sega Genesis Mini", ["Sega"], datetime(2019, 9, 19), ["Negro", "Rojo"], True, 512, 2),
    ConsolaSobreMesa("Atari VCS", ["Atari"], datetime(2020, 6, 15), ["Negro"], False, 1000, 4),
    ConsolaSobreMesa("PlayStation 4 Pro", ["Sony"], datetime(2016, 11, 10), ["Negro"], False, 1000, 3),
    ConsolaSobreMesa("Xbox One X", ["Microsoft"], datetime(2017, 11, 7), ["Negro"], False, 1000, 3),
    ConsolaSobreMesa("Nintendo Classic Mini", ["Nintendo"], datetime(2016, 11, 11), ["Gris"], True, 512, 2),
    ConsolaSobreMesa("Neo Geo Mini", ["SNK"], datetime(2018, 7, 24), ["Negro", "Rojo"], True, 256, 2),
    ConsolaSobreMesa("PlayStation Classic", ["Sony"], datetime(2018, 12, 3), ["Gris"], True, 256, 2),
    ConsolaSobreMesa("PlayBox Fusion", ["Sony", "Microsoft"], datetime(2025, 3, 1), ["Negro", "Plata"], False, 2000, 4),
    ConsolaSobreMesa("NintenBox", ["Nintendo", "Microsoft"], datetime(2024, 11, 20), ["Rojo", "Negro"], True, 1000, 3),
    ConsolaSobreMesa("SegaStation Ultra", ["Sega", "Sony"], datetime(2023, 9, 5), ["Azul", "Gris"], False, 1500, 4),
    ConsolaSobreMesa("Atari Cube X", ["Atari", "Nintendo"], datetime(2022, 7, 15), ["Negro", "Marrón"], False, 512, 2),
    ConsolaSobreMesa("NeoGeo Legend", ["SNK", "Capcom"], datetime(2021, 5, 10), ["Negro", "Rojo"], True, 256, 2)
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

print("-" * 140)

print("consolas con los colores Negro y rojo:")
for consola in consolas_sobremesa:
    if consola.filtrar_colores("Negro", "Rojo") == True:
        print(consola)