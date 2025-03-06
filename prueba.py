#ejercicio 36. Crea un programa que dado un número te muestre la tabla de multiplicar de dicho número.

num = int(input("Introduzca un número: "))

numTabla = 0

for i in range(10):
    i = i + 1
    operacion = num * i
    print(f"Operación {i} {num} x {i} = {operacion}")

#Ejercicio 40. Crea un programa calcule el número de veces que aparece dicha letra en el texto. 

def contar_letra_en_texto (letra: str, texto: str):
    
    n_veces = 0
    caracter = letra

    for letra in texto:
        if caracter == letra:
            n_veces = n_veces + 1

    return n_veces

texto = input("Introduzca texto: ")
letra = input("Introduzca una letra: ")

n_letras = contar_letra_en_texto(letra, texto)
print(n_letras)