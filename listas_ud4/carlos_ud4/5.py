def pais_mayor_densidad(continente: str, paises: list) -> str:
    max_densidad = 0
    pais_max_densidad = ""
    for pais in paises:
        if pais[3] == continente:
            poblacion = pais[2]
            area = pais[4]
            densidad = poblacion / area
            if densidad > max_densidad:
                max_densidad = densidad
                pais_max_densidad = pais[0]
    return pais_max_densidad