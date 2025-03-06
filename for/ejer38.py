num = int(input("Inserte un número: "))

for i in range(2,(num+1)):
    if num % i == 0:
        print("El número no es primo")
        break
    else:
        print("El número es primo")
        break
