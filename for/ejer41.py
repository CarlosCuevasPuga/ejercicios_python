texto = input("Introduzca un texto: ")
npalabras = 0

for letra in texto:
    if letra == " ":
        npalabras = npalabras + 1
print(f"En el texto hay {npalabras + 1} palabras")