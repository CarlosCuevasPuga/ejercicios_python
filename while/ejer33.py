num = int(input("Ingresa un número: "))
fact = 1
i=0

while i != num:
    i = i + 1
    fact = i * fact
print(f"El factorial de {num} es {fact}")