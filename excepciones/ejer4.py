numMayor = 0
numMenor = 0
intentos = 0
media_numeros = 0
numUsuario = 0

while True:
    try:
        numUsuario = int(input("Introduce un número (0 para salir): "))
        media_numeros += numUsuario
        if numUsuario == 0:
            break
        elif numUsuario > numMayor:
            numMayor = numUsuario
        elif numUsuario < numMenor:
            numMenor = numUsuario
        intentos += 1
    except ValueError as error:
        print(f"[ERROR] Usted a introducido un tipo de dato no valido {error}")

print(intentos)
print(f"El número mayor es {numMayor} y el menor es {numMenor}")
print(f"La media es {round(media_numeros / intentos, 1)}")
