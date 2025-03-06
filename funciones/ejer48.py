import random
import math
inicio = float(input("Introduzca el número inicial: "))
fin = float(input("Introduzca el número final: "))
nVeces = int(input("¿Cuantos números quieres ver?: "))

for i in range(nVeces):
    aleatorio = math.floor(inicio + (fin - inicio) * random.random(),2)
    print(aleatorio)