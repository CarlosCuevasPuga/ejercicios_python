matriz = [
    ["Juanillo", 4, 1, 5],
    ["Marta", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

i = 3

for fila in matriz:
    media = round(sum(fila[1:]) / i, 1)
    print(f"La media de {fila[:1]} es {media}")
            