def suma_matrices(m1: list, m2: list) -> list:
    resultado = []
    for i in range(len(m1)):
        fila_resultado = []
        for j in range(len(m1[i])):
            fila_resultado.append(m1[i][j] + m2[i][j])
        resultado.append(fila_resultado)
    return resultado