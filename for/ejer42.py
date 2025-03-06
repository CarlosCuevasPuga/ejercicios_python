texto = input("Introduzca un texto: ")
nvocales = 0

for letra in texto:
    if letra == "a" or letra == "A":
        nvocales = nvocales + 1
    if letra == "e"or letra == "E":
        nvocales = nvocales + 1
    if letra == "i" or letra == "I":
        nvocales = nvocales + 1
    if letra == "o" or letra == "O":
        nvocales = nvocales + 1
    if letra == "u" or letra == "U":
        nvocales = nvocales + 1
print(f"En el texto hay {nvocales} vocales")