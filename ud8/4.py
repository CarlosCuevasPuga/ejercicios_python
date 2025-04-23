# No terminado
with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contar_caracteres = 0
    for linea in lineas:
        for palabra in linea:
            for caracter in palabra:
                contar_caracteres += 1

media = round(contar_caracteres/len(lineas), 1)
print(f"De media son {media} caracteres por linea")