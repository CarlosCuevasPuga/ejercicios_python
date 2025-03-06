import random


def info_partida(dedos_usuario: int, dedos_bot: int) -> int:
    print(f"Has sacado {dedos_usuario} dedos")
    print(f"El bot ha sacado {dedos_bot} dedos")
    suma_total = dedos_usuario + dedos_bot
    print(f"La suma total es: {suma_total}")


def comprobacion_pares_nones(eleccion_usuario: str, dedos_usuario: int, dedos_bot: int):
    if dedos_usuario % dedos_bot == 0 and eleccion_usuario == "pares":
        info_partida(dedos_usuario, dedos_bot)
        print("Has ganado")
    elif dedos_usuario % dedos_bot != 0 and eleccion_usuario == "pares":
        info_partida(dedos_usuario, dedos_bot)
        print("Ha ganado el bot")
    elif dedos_usuario % dedos_bot != 0 and eleccion_usuario == "nones":
        info_partida(dedos_usuario, dedos_bot)
        print("Has ganado")
    else:
        info_partida(dedos_usuario, dedos_bot)
        print("Ha ganado el bot")

try:
    eleccion_usuario = input("Introduzca pares o nones: ")
    while True:
        print("[ERROR] Solo se permite elegir 'pares' o 'nones'")
        eleccion_usuario = input("Introduzca pares o nones: ")
        if eleccion_usuario == "pares" or eleccion_usuario == "nones":
            break
    dedos_usuario = int(input("Inserte el número de dedos que quieres sacar: "))
    dedos_bot = random.randint(0, 21)
except ValueError as error:
    print(f"[ERROR] Ha introducido un tipo de dato no valido {error}")
except Exception as error:
    print(f"[ERROR] Ha ocurrido un error {error}")
else:
    comprobacion = comprobacion_pares_nones(eleccion_usuario, dedos_usuario, dedos_bot)
