i = 1
palabra_larga = 0
palabra_corta = 0
while True:
    texto = input("Inserte texto (escriba fin para terminar): ")
    if texto == "fin":
        break
    if i == 1:
        palabra_larga = texto
        palabra_corta = texto
    else:
        if len(texto) > len(palabra_larga):
            palabra_larga = texto
        if len(texto) < len(palabra_corta):
            palabra_corta = texto
    i = i + 1
print(f"La palabra mas larga es {palabra_larga} y la mas corta es {palabra_corta}")