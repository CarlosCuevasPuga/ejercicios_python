def CambioTemperatura(opcion: str, grados: float):
    if opcion == "Fharenheit":
        try:
            calculo = (grados * 9 / 5) + 32
        except TypeError as ValorNoValido:
            print(f"[ERROR] usted a introducido un número (solo se permite Fharenheit o Celsius): {ValorNoValido}")
        else:
            if opcion != "Fharenheit":
                raise TypeError ("[ERROR] usted a introducido mal el nombre 'Fharenheit' o 'Celsius'")
        finally:
            print(calculo)
    elif opcion == "Celsius":
        try:
            calculo = (grados - 32) * 0.5556
        except TypeError as ValorNoValido:
            print(f"[ERROR] usted a introducido un número (solo se permite Fharenheit o Celsius): {ValorNoValido}")
        else:
            if opcion != "Celsius":
                raise TypeError ("[ERROR] usted a introducido mal el nombre 'Fharenheit' o 'Celsius'")
        finally:
            calculo = (grados * 9 / 5) + 32
    return calculo

opcion = input("Introduzca que temperatura quiere calcular: ")
grados = input("Introduzca los grados a calcular: ")

print(CambioTemperatura(opcion, grados))
