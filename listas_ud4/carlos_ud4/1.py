def poblacion_media(poblaciones: list) -> float:
    media = sum(poblaciones) / len(poblaciones)
    return media

def pais_menos_poblado(poblaciones: list, paises: list) -> str:
    menos_poblado = min(poblaciones)
    pos_pais = poblaciones.index(menos_poblado)
    return paises[pos_pais]

paises = ["Alemania", "Francia", "Italia", "España", "Países Bajos", "Polonia", "Suecia", "Bélgica", "Austria", "Portugal"]

poblaciones = [83, 68, 59, 47, 17, 38, 10, 11, 9, 10]  # En millones de habitantes

media = poblacion_media(poblaciones)
pais_menor = pais_menos_poblado(poblaciones, paises)

print(f"La población media es: {round(media, 2)}")
print(f"El nombre del pais menos poblado es: {pais_menor}")