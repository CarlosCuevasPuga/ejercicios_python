from Planeta import Planeta
from datetime import datetime

planetas_sistema_solar = [
    Planeta("Mercurio", 3.301e23, 2.4397e6, datetime.min, []),
    Planeta("Venus", 4.867e24, 6.0518e6, datetime.min, []),
    Planeta("Tierra", 5.972e24, 6.371e6, datetime.min, [["Luna", 1.737e6, 7.342e22]]),
    Planeta("Marte", 6.417e23, 3.3895e6, datetime.min, [["Fobos", 1.1e4, 1.0659e16], ["Deimos", 6.2e3, 1.4762e15]]),
    Planeta("Júpiter", 1.898e27, 6.9911e7, datetime.min, [["Ganimedes", 2.634e6, 1.0659e16], ["Calisto", 2.410e6, 1.0759e23], ["Ío", 1.821e6, 8.9319e22], ["Europa", 1.560e6, 4.7998e22]]),
    Planeta("Saturno", 5.683e26, 5.8232e7, datetime.min, [["Titán", 2.572e6, 1.3452e23], ["Rea", 1.527e6, 2.3166e21], ["Japeto", 1.470e6, 1.8056e21], ["Dione", 1.123e6, 1.0955e21]]),
    Planeta("Urano", 8.681e25, 2.5362e7, datetime.min, [["Titania", 1.578e6, 3.527e21]]),
    Planeta("Neptuno", 1.024e26, 2.4622e7, datetime.min, [["Tritón", 1.353e6, 2.14e22]]),
    Planeta("Plutón", 1.303e22, 1.1883e6, datetime(1930, 2, 18), [["Caronte", 6.057e5, 1.586e21]])
]

planetas_trappist = [
    Planeta("TRAPPIST-1b", 0.85 * 5.972e24, 1.116 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1c", 1.38 * 5.972e24, 1.097 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1d", 0.388 * 5.972e24, 0.788 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1e", 0.692 * 5.972e24, 0.920 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1f", 1.04 * 5.972e24, 1.045 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1g", 1.32 * 5.972e24, 1.127 * 6.371e6, datetime(2017, 2, 22), []),
    Planeta("TRAPPIST-1h", 0.326 * 5.972e24, 0.755 * 6.371e6, datetime(2017, 2, 22), [])
]

# masa media de los planetas del Sistema Solar vs la masa media de lo planetas de TRAPPIST-1
masas_sistema_solar = [planeta.masa for planeta in planetas_sistema_solar]
masa_media_sistema_solar = sum(masas_sistema_solar) / len(planetas_sistema_solar)

masas_trappist = [planeta.masa for planeta in planetas_trappist]
masa_media_trappist = sum(masas_trappist) / len(planetas_trappist)

if masa_media_sistema_solar > masa_media_trappist:
    print(f"La masa media del sistema solar ({masa_media_sistema_solar}) es mayor que la masa media de trappist ({masa_media_trappist})")
else:
    print(f"La masa media de trappist ({masa_media_trappist}) es mayor que la masa media del sistema solar ({masa_media_sistema_solar})")

# planeta más denso de ambos sistemas
densidad_planetas_sistema_solar = [planeta.get_densidad() for planeta in planetas_sistema_solar]
densidad_planetas_trappist = [planeta.get_densidad() for planeta in planetas_trappist]

densidad_mayor_sistema_solar = max(densidad_planetas_sistema_solar)
densidad_mayor_trappit = max(densidad_planetas_trappist)

for planeta in planetas_sistema_solar:
    if densidad_mayor_sistema_solar == planeta.get_densidad():
        planeta_mayor_densidad_sistema_solar = planeta.nombre

for planeta in planetas_trappist:
    if densidad_mayor_trappit == planeta.get_densidad():
        planeta_mayor_densidad_trappist = planeta.nombre

print(f"El planeta con la mayor densidad del sistema solar es: {planeta_mayor_densidad_sistema_solar}")
print(f"El planeta con la mayor densidad de trappist es: {planeta_mayor_densidad_trappist}")

# planeta de TRAPPIST-1 cuya densidad más se parece a la de la Tierra
densidad_tierra = 0

for planeta in planetas_sistema_solar:
    if planeta.nombre == "Tierra":
        densidad_tierra = planeta.get_densidad()

for iplaneta in planetas_trappist:
    pass

# planetas sin lunas de ambos sistemas
planetas_sistema_solar_luna = [planeta.lunas for planeta in planetas_sistema_solar]
planetas_sistema_solar_sin_luna = []

for i, planeta in enumerate(planetas_sistema_solar):
    if planeta != planetas_sistema_solar_luna[i]:
        planetas_sistema_solar_sin_luna.append(planeta)

for planeta in planetas_sistema_solar_sin_luna:
    print(planeta)