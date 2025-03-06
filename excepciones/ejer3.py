numSecreto = 56
num_intentos = 0

while True:
    try:
        opcion = int(input("Adivine el número: "))
    except ValueError as error:
        print(f"[ERROR] Usted a introducido un tipo de dato no valido {error}")
    else:
        num_intentos += 1
        if opcion == numSecreto:
            break
        elif opcion < numSecreto:
            print("El número secreto es mayor")
        else:
            print("El número secreto es menor")

print("Has acertado !!!")
print(f"Lo has intentado: {num_intentos}")
