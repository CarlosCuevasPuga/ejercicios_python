matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

vocales = ["A","E","I","O","U"]
i = 0

for fila in matriz:
    for nombre in fila:
        for letra in vocales:
            if nombre[0] == letra:
                print(nombre)