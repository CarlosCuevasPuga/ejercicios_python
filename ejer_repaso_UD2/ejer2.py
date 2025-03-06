num_veces = 0
mayor = 0
menor = 0

while num_veces != 10:
    num = int(input("Introduce un número: "))

    if num_veces == 0:
        mayor = num
        menor = num

    if num > mayor:
        mayor = num
    elif num < menor:
        menor = num

    num_veces = num_veces + 1

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")