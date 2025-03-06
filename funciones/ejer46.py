import math

while True:
    a = int(input("Introduzca el valor de a: "))
    if a == 0:
        break
    b = int(input("Introduzca el valor de b: "))
    c = int(input("Introduzca el valor de c: "))
    resultado1 = b + math.sqrt(b**2-4*a*c)/2*a
    resultado2 = b - math.sqrt(b**2-4*a*c)/2*a

    print(f"El primer resultado es {resultado1}")
    print(f"El segundo resultado es {resultado2}")
    break