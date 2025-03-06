def comprobar_n(lista: list, n: int) -> bool:
    mayor_o_igual = False
    if min(lista) == n:
        mayor_o_igual = True
    return mayor_o_igual