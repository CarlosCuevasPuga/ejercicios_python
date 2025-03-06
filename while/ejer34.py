num_usuario = int(input("Intente adivinar el número secreto (del 1 al 50): "))
num_secreto = 30
intentos = 0

while num_usuario != num_secreto:
    if num_usuario < num_secreto:
        print("El número secreto es mayor")
        intentos = intentos + 1
        num_usuario = int(input("vuelva a intentarlo (del 1 al 50): "))
    else:
        print("El número secreto es menor")
        intentos = intentos + 1
        num_usuario = int(input("vuelva a intentarlo (del 1 al 50): "))

print("!!!! Felicidades !!!!")
print(f"Has tardado {intentos} intentos")