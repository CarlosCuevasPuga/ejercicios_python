import math

a = 0
b = 0
c = 0

while True:
    try:
        a = int(input("Inserte el valor de a: "))
        b = int(input("Inserte el valor de b: "))
        c = int(input("Inserte el valor de c: "))
        if a == 0:
            break
    except ValueError as error:
        print(f"[ERROR] Solo se permiten números {error}")
    else:
        if a < 0 and c > 0:
            primer_calculo = - b + math.sqrt(b * b - 4 * a * c) / 2 * a
            segundo_calculo = - b - math.sqrt(b * b - 4 * a * c) / 2 * a
            print(f"El primer resultado es: {primer_calculo}")
            print(f"El segundo resultado es: {segundo_calculo}")
        else:
            print("[ERROR] El valor de a solo puede ser negativo y c solo puede ser positivo")
