def sin_repetidos(lista_nums: list) -> list:
    copia_lista = lista_nums.copy()
    lista_sin_repe = []
    for n in copia_lista:
        if lista_sin_repe.count(n) == 0:
            lista_sin_repe.append(n)
    return lista_sin_repe

nums = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]

lista_sin_repe = sin_repetidos(nums)

print(lista_sin_repe)