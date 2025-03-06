import random
inicio = int(input("Introduzca el número inicial: "))
fin = int(input("Introduzca el número final: "))
nVeces = int(input("¿Cuantos números quieres ver?: "))

for i in range(nVeces):
    print(random.randint(inicio,fin))