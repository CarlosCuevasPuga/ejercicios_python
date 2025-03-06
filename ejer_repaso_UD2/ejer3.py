# Variable para almacenar el primer número ingresado
num = None

# Variable para controlar si se repite un número
num_repetido = False

while not num_repetido:
    # Solicitar un número al usuario
    num_input = int(input("Introduce un número: "))

    # Comprobar si el número ya ha sido ingresado antes
    if num == num_input:
        num_repetido = True
    else:
        # Si es el primer número o no se repite, guardarlo
        num = num_input

print("Has introducido un número repetido. Fin del programa.")