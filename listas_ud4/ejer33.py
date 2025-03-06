palabras = []

while True:
    palabra = input("Inserta una palabra: ")
    if palabra == "fin":
        break
    palabras.append(palabra)

palabras.sort()
print(palabras)