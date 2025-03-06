def es_cuadrada(m: list) -> bool:
    cuadrada = None
    for i, fila in enumerate(m):
        for j, columna in enumerate(fila):
            if i == columna:
                cuadrada = True
            else:
                cuadrada = False
    return cuadrada

            

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

cuadrada = es_cuadrada(m)

print(cuadrada)