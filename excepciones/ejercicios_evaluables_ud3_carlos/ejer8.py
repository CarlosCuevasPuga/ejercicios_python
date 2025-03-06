# preguntarle a borja si puede haber catetos negativos

import math

cateto_1 = 0
cateto_2 = 0

try:
    cateto_1 = int(input("Introduce el valor del primer cateto: "))
    cateto_2 = int(input("Introduce el valor del segundo cateto: "))
except ValueError as error:
    print(f"[ERROR] Se ha introducido un dato no valido {error}")
except Exception as error:
    print(f"[ERROR] Se ha producido un error {error}")
else:
    hipotenusa = math.sqrt(cateto_1 * cateto_1 + cateto_2 * cateto_2)
    print(f"La hipotenusa de {cateto_1} y {cateto_2} es {hipotenusa}")
