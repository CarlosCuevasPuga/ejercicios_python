from datetime import datetime
from ConsolaSobreMesa import ConsolaSobreMesa
from ConsolaPortatil import ConsolaPortatil
from ColeccionConsolas import Tienda

consolas_sobremesa = [
    # Consolas de sobremesa
    ConsolaSobreMesa("PlayStation 5", ["Sony"], datetime(2020, 11, 12), ["Blanco", "Negro"], False, 825, 4),
    ConsolaSobreMesa("Xbox Series X", ["Microsoft"], datetime(2020, 11, 10), ["Negro"], False, 1000, 3),
    ConsolaSobreMesa("PlayBox Fusion", ["Sony", "Microsoft"], datetime(2025, 3, 1), ["Negro", "Plata"], False, 2000, 4),
    ConsolaSobreMesa("NintenBox", ["Nintendo", "Microsoft"], datetime(2024, 11, 20), ["Rojo", "Negro"], True, 1000, 3),
    ConsolaSobreMesa("Neo Geo Mini", ["SNK", "Capcom"], datetime(2018, 7, 24), ["Negro", "Rojo"], True, 256, 2),
]

consolas_portatiles = [
    # Consolas portátiles
    ConsolaPortatil("Nintendo Switch", ["Nintendo"], datetime(2017, 3, 3), ["Rojo", "Azul"], False, 32, 9),
    ConsolaPortatil("Steam Deck", ["Valve"], datetime(2022, 2, 25), ["Negro"], False, 512, 8),
    ConsolaPortatil("PlayGo", ["Sony", "Google"], datetime(2023, 6, 10), ["Gris", "Negro"], False, 256, 10),
    ConsolaPortatil("Neo Pocket Duo", ["SNK", "Sega"], datetime(2021, 10, 1), ["Blanco", "Azul"], True, 128, 12),
    ConsolaPortatil("Atari Mini Handheld", ["Atari"], datetime(2020, 5, 5), ["Negro", "Naranja"], False, 64, 7)
]

coleccion_consolas = Tienda()
for consola in consolas_sobremesa:
    coleccion_consolas.meter_consolas_sobremesa(consola)
for consola in consolas_portatiles:
    coleccion_consolas.meter_consolas_portatil(consola)

while True:

    print(coleccion_consolas)

    print("¿Qué deseas hacer?")
    print("[A]ñadir")
    print("[O]rdenar (por fecha de salida)")
    print("[S]alir")

    opcion_menu = input("").upper()
    if opcion_menu == "S":
        break

    elif opcion_menu == "A":
        pass

    elif opcion_menu == "O":
        print("\n## Consolas ordenadas por fecha de salida:")
        coleccion_ordenada_fecha = coleccion_consolas.ordenar_por_fecha()
        for consola in coleccion_ordenada_fecha:
            fecha = consola.fecha_salida.strftime("%d/%m/%Y")
            print(f"{consola.nombre} -- {fecha}")
        input()

    else:
        num_consola = int(opcion_menu)
        
        if num_consola > 0:
            consola_a_mostrar = coleccion_consolas.mostrar(num_consola)
            print(consola_a_mostrar)
            input()

        elif num_consola < 0:
            juego_a_borrar = coleccion_consolas.mostrar(num_consola)
            print(f"Va a proceder a borrar la consola: {juego_a_borrar.nombre} con {juego_a_borrar.almacenamiento} MB de memoria")
            opcion_borrar = input("¿Está Seguro (S/N)?").upper()

            if opcion_borrar == "S":
                coleccion_consolas.borrar(num_consola)
                print("Consola Eliminada")

            elif opcion_borrar == "N":
                print("Eliminacion Cancelada")
            input()