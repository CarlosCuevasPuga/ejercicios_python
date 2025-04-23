with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len([palabra for palabra in lineas if len(palabra.split()) > 0 and ("caballero" in palabra.split() or "Caballero" in palabra.split())])

print(f"El Quijote tiene {contador} lineas que tengan caballero o Caballero")