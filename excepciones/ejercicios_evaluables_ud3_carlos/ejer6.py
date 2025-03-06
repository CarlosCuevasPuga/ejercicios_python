import random

while True:
    try:
        inicio = int(input("Introduce el número inicial: "))
        fin = int(input("Introduce el número final: "))
    except ValueError as error:
        print(f"[ERROR] Usted a introducido un dato no valido {error}")
    except Exception as error:
        print(f"[ERROR] Se ha producido un error {error}")
    else:
        if inicio < fin:
            for i in range(inicio, fin):
                nVeces = round(random.random(), 2)
                print(nVeces)
        else:
            print("El número inicial no puede ser mayor que el final")
