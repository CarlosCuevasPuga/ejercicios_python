base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
caracter = input("Ingrese el caracter:" )

print("Dibujo del rectangulo: ") 

i = 1
linea = caracter

while i < base:
    linea = linea + caracter

    i = i + 1

i = 0
while i < altura:
    print(linea)
    i = i + 1