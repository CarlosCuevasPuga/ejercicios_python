def tabla(num: int):
    for i in range(11):
        calculo = i * num
        print(f"{i} x {num} = {calculo}")
        i = i + 1

num = int(input("Inserta un número: "))

tabla(num)