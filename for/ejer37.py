num = int(input("Ingresa un número: "))
fact = 1

for i in range(1,(num+1),1):
    fact = i * fact

print(f"El factorial de {num} es {fact}")