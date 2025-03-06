Tipovia = "Autovia"
Tipovehiculo = "Coche"

velocidad_max = -1

if Tipovia == "Autovia":
    if Tipovehiculo == "Coche":
        velocidad_max == 120
    elif Tipovehiculo == "Bus":
        velocidad_max == 110
    elif Tipovehiculo == "Camión":
        velocidad_max == 100
    elif Tipovia == "Nacional":
        if Tipovehiculo == "Coche" or Tipovehiculo == "Bus":
            velocidad_max == 100
        elif Tipovehiculo == "Camión":
            velocidad_max == 90

print(f"El tipo de vheiculo {Tipovehiculo} por el tipo de vía {Tipovia} su velocidad maxima es {velocidad_max}")