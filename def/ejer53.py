def longitud(palabra: str) -> int:
    vocales = 0

    for vocal in palabra:
        if vocal == "a" or vocal == "A":
            vocales = vocales + 1
        if vocal == "e" or vocal == "E":
            vocales = vocales + 1
        if vocal == "i" or vocal == "I":
            vocales = vocales + 1
        if vocal == "o" or vocal == "O":
            vocales = vocales + 1
        if vocal == "u" or vocal == "U":
            vocales = vocales + 1

    return vocales

palabra = input("Escribe una palabra: ")

nVocales = longitud(palabra)

print(f"{nVocales}")