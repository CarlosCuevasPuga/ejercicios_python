def radio_medio_gaseosos(planetas: list) -> float:
    suma_gaseosos = 0
    for i, fila in enumerate(planetas):
        for j, colum in enumerate(fila):
            if colum == False:
                radio = fila[-1:]
                suma_gaseosos += sum(radio)
    return suma_gaseosos / i

def radio_medio_rocosos(planetas: list) -> float:
    suma_rocosos = 0
    for i, fila in enumerate(planetas):
        for j, colum in enumerate(fila):
            if colum == True:
                radio = fila[-1:]
                suma_rocosos += sum(radio)
    return suma_rocosos / i

def mas_grande_rocoso_gaseoso(planetas: list):
    radio_rocoso_mayor = 0
    for i, fila in enumerate(planetas):
        for j, columna in enumerate(planetas):
            pass

def nombres_en_no(planetas: list):
    for fila in planetas:
        for j, nombre in enumerate(fila[:1]):
            if nombre[-2:] == "no":
                print(nombre)

planetas = [
    ["Mercurio", True, 2439.7],
    ["Venus", True, 6051.8],
    ["Tierra", True, 6371.0],
    ["Marte", True, 3389.5],
    ["Júpiter", False, 69911],
    ["Saturno", False, 58232],
    ["Urano", False, 25362],
    ["Neptuno", False, 24622],
    ["Plutón", True, 1188.3]  # Incluyendo a Plutón
]

media_gaseosos = radio_medio_gaseosos(planetas)
media_rocosos = radio_medio_rocosos(planetas)

print(f"El radio medio de los gaseosos es: {media_gaseosos}")
print(f"El radio medio de los rocosos es: {media_rocosos}")
nombres_en_no(planetas)