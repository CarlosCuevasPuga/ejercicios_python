import random

def imprimir_menu(vidas: int, nivel: int):

    print("--------------------")
    print(f"Nivel {nivel}")
    print("--------------------")
    print(f"Tienes {vidas} vidas")

def elegir_palabra_aleatoria(lista_palabras: list):
    num_aleatorio = random.randint(0, len(lista_palabras)-1)
    palabra_aleatoria = lista_palabras[num_aleatorio]
    return palabra_aleatoria

def comprobar_letra(palabra_aleatoria: str, lista_letras: list, letra_usuario: str):
    for i, letra in enumerate(lista_letras):
        if palabra_aleatoria[i] == letra_usuario:
            return letra

def comprobar_letra_repetida(lista_insertadas: list, letra_usuario: str) -> bool:
    insertada = False
    for letra_insertada in lista_insertadas:
        if letra_insertada == letra_usuario:
            insertada = True
    return insertada