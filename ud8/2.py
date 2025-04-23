with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len([palabra for palabra in lineas if len(palabra.split()) > 0 and palabra.split()[0].lower() == "don"])

print(f"El Quijote tiene {contador} lineas que empiezan por don")