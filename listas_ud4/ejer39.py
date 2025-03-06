palabras = input("Inserta palabras separadas por coma: ").split(",")
menor = palabras[0]
mayor = palabras[0]

for palabra in palabras:
    if len(palabra) > len(mayor):
        mayor = palabra
    else:
        menor = palabra

print(f"La palabra con menos letras es {menor}")
print(f"La palabra con mas letras es {mayor}")