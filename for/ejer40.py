texto = input("Introduzca un texto: ")
letra = input("Introduce la letra: ")
nletras = 0

for caracter in texto:
    if caracter == letra:
        nletras = nletras + 1
print(f"En el texto hay {nletras} letra/s {letra}")