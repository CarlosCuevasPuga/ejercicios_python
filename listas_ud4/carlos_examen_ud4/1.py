def animal_menos_peso(pesos_animales: list, animales_domesticos: list):
    menos_peso = pesos_animales[0]
    for peso in pesos_animales:
        if menos_peso > peso:
            menos_peso = peso
    index_menos_peso = pesos_animales.index(menos_peso)
    return index_menos_peso

def nombre_mayor_media (pesos_animales: list, animales_domesticos: list) -> str:
    media = sum(pesos_animales) / 2

    for i, peso_animal in enumerate(pesos_animales):
        if media > peso_animal:
            return animales_domesticos[i]

animales_domesticos = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]

pesos_animales = [10, 4, 2, 0.1, 0.3, 0.2, 1.5, 1, 1.2, 0.05]

index_menos_peso = animal_menos_peso(pesos_animales, animales_domesticos)

nombre = nombre_mayor_media(pesos_animales, animales_domesticos)

print(f"El animal que menos pesa es el {animales_domesticos[index_menos_peso]}")
print(f"Los animales que pesan mas que la media son: {nombre}")
