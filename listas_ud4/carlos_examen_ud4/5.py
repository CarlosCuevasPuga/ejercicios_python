import random

def generar_partitura(longitud: int, nRepeticiones: int) -> list:
    lista_notas = []
    for _ in range(longitud):
        num_aleatorio = random.randint(1, 7)
        if num_aleatorio == 1:
            lista_notas.append("DO")
        elif num_aleatorio == 2:
            lista_notas.append("RE")
        elif num_aleatorio == 3:
            lista_notas.append("MI")
        elif num_aleatorio == 4:
            lista_notas.append("FA")
        elif num_aleatorio == 5:
            lista_notas.append("SOL")
        elif num_aleatorio == 6:
            lista_notas.append("LA")
        elif num_aleatorio == 7:
            lista_notas.append("SI")
    return lista_notas

lista_notas = generar_partitura(20, 2)
print(lista_notas)