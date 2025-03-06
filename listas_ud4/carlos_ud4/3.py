import random

def emparejamiento_aleatorio(tenistas: list):
    emparejamientos = []

    while len(tenistas) > 1:

        index1 = random.randint(0, len(tenistas) - 1)
        tenista1 = tenistas.pop(index1)

        index2 = random.randint(0, len(tenistas) - 1)
        tenista2 = tenistas.pop(index2)
        
        emparejamientos.append((tenista1, tenista2))
    for nombre in emparejamientos:
        print(f"{nombre[0]} vs {nombre[1]}")
    

tenistas_top_8 = [
    "Jannik Sinner",      # 11,330 puntos
    "Alexander Zverev",   # 8,135 puntos
    "Carlos Alcaraz",     # 7,410 puntos
    "Taylor Fritz",       # 4,900 puntos
    "Casper Ruud",        # 4,480 puntos
    "Daniil Medvedev",    # 3,930 puntos
    "Novak Djokovic",     # 3,900 puntos
    "Álex de Miñaur"      # 3,735 puntos
]

print("ENFRENTAMIENTOS:")
emparejamiento_aleatorio(tenistas_top_8)