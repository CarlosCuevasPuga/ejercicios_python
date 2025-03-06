i=1

while True:

    num = int(input("Introduzca un número (0 para salir): "))
    if i == 1:
        num_mayor = num 
        num_menor = num
    if num == 0:
        break

    if num > num_mayor:
        num_mayor = num
    if num < num_menor:
        num_menor = num

    i= i + 1
print(f"El numero mayor es {num_mayor} y el menor es {num_menor}")