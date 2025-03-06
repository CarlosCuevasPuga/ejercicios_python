def circunferencia(radio: float) -> float:
    calculo = 2*3.14*radio
    return calculo

radio = float(input("Introduzca el radio del circulo: "))

resultado = circunferencia(radio)
print(f"La longitud de la circunferencia es: {resultado}")