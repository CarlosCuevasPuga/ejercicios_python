with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len([linea for linea in lineas if linea[0].lower() == "a"])

print(f"El Quijote tiene {contador} lineas que empiezan por a")