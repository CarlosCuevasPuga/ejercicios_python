import math

while True:
    try:
        num = int(input("Inserte un número: "))
    except ValueError as error:
        print(f"[ERROR] Usted a insertado un tipo de dato no valido {error}")
    else:
        if num == 0 or num < 0:
            break
        else:
            raiz_cuadrada = math.sqrt(num)
            print(f"La raiz cuadrada de {num} es: {raiz_cuadrada}")
