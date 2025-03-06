import math
def hipo(cateto1:float , cateto2:float) -> float:
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

    return hipotenusa

cateto1 = float(input("Introduce la longitud del primero cateto: "))
cateto2 = float(input("Introduce la longitud del segundo cateto: "))

resultado = hipo(cateto1,cateto2)

print(f"La hipotenusa de {cateto1} y {cateto2} es {resultado}")