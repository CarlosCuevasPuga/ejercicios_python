matriz = [
    [4, -2, 3],
    [3, 4, 2],
    [7, 5, 9],
    [1, 0, -1]
]

fila_lista = 0
columna_lista = 0

for i, fila in enumerate(matriz):
    for j, num in enumerate(fila):
        if num == 5:
            fila_lista = i
            columna_lista = j

print(f"El 5 está en la fila {fila_lista}, columna {columna_lista}")

for i, fila in enumerate(matriz):
    if fila.count(5)>0:
        fila_lista = i
        columna_lista = fila.index(5)
        break

print(f"El 5 está en la fila {fila_lista} y la columna {columna_lista}")