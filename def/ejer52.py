import random

def caraCruz(nVeces: int):
    for i in range(nVeces):
        azar = random.randint(1,2)
        if azar == 1:
            eleccion = "cara"
            print(f"{eleccion}")
        elif azar == 2:
            eleccion = "cruz"
            print(f"{eleccion}")

nVeces = int(input("Cuantas veces quieres tirar la moneda: "))

caraCruz(nVeces)