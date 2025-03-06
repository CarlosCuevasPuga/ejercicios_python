planetas = [
    "Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"
]

masas = [
    0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102
]

radios = [
    2439, 6052, 6371, 3389, 69911, 58232, 25362, 24622
]

pos_planeta = 0

while True:
    nombre_planeta = input("Introduce el nombre del planeta: ")
    pos_planeta = planetas.index(nombre_planeta)
    print(f"Su masa es: {masas[pos_planeta]}")
    print(f"Su radio es: {radios[pos_planeta]}")