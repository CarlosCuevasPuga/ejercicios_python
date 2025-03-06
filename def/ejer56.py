def longitud(frase: str) -> int:
    palabras = 1
    for palabra in frase:
        if palabra == " ":
            palabras = palabras + 1

    return palabras

frase = input("Escribe una frase: ")

nPalabras = longitud(frase)

print(f"En la frase hay {nPalabras} palabras")