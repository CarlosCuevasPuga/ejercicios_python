with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    linea_mas_larga = ""
    contador = 0
    for caracter in lineas:
        if len(caracter.split()) > 0 and caracter > linea_mas_larga:
            linea_mas_larga = caracter

print(f"La linea mas larga es {linea_mas_larga} y tiene {len(linea_mas_larga)} caracteres")