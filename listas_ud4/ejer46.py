matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

nums = [1,2,3]

suma = 0

for fila in matriz:
    for num in fila:
        suma += num

print(suma)

sumaTotal = 0

for fila in matriz:
    sumaTotal += sum(fila)

print(sumaTotal)