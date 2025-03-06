animales_domesticos = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]

pesos_animales = [
    [5, 40],   # Perro (depende de la raza)
    [2, 8],    # Gato
    [1, 3],    # Conejo
    [0.08, 0.25], # Hámster
    [0.2, 1.5],   # Loro
    [0.1, 2],  # Pez (varía mucho según la especie)
    [0.5, 2],  # Tortuga (pequeñas domésticas)
    [0.7, 1.5],  # Cobaya
    [0.5, 2],  # Hurón
    [0.02, 0.06] # Canario
]

mayor_diferencia = pesos_animales[0]

for i, pesos in enumerate(pesos_animales):
    if pesos > pesos_animales[0]:
        mayor_diferencia = pesos

index_pesos = pesos_animales.index(mayor_diferencia)
print(f"El animal con mas diferencia de peso es el {animales_domesticos[index_pesos]}")