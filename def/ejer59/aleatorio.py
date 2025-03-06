import random

def lanzarMoneda():
    tirada = random.randint(1,2)
    if tirada == 1:
        print("Cara")
    elif tirada == 2:
        print("Cruz")

def lanzarMonedas(nMonedas: int):
    for _ in range(nMonedas):
        lanzarMoneda()

def lanzarDado():
    tirada = random.randint(1,6)
    print(tirada)

def lanzarDados(nDados):
    for _ in range(nDados):
        lanzarDado()