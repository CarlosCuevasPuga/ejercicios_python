numSecreto = 60
intentos = 0
num_Usuario = int(input("Intente advinar el número secreto (del 1 al 100): "))

while numSecreto != num_Usuario:
    if numSecreto > num_Usuario:
        print("Has fallado, el número secreto es mayor")
        num_Usuario = int(input("vuelve a intentarlo: "))
        intentos = intentos + 1
    else:
        print("Has fallado, el número secreto es menor")
        num_Usuario = int(input("vuelve a intentarlo: "))
        intentos = intentos + 1

print("!!! Has acertado !!!")
print(f"Has tardado {intentos} intentos")