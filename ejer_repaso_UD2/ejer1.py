def calculo(tipo_habitacion: str, vistas_mar: str, dias: int) -> float:

    if tipo_habitacion == "individual" and vistas_mar == "si":
        precio = 4800
    elif tipo_habitacion == "individual" and vistas_mar == "no":
        precio = 1600
    elif tipo_habitacion == "doble" and vistas_mar == "si":
        precio = 8000
    else:
        precio = 2400

    precio_total = 0
    precio_total = precio * dias

    if dias >= 7:
        dias_descuento = 0
        precio_sin_descuento = 0

        dias_descuento = dias - 6  
        descuento = (precio * dias_descuento) * (2 / 100)
        precio_total = (precio * 6) + (precio * dias_descuento) - descuento

    return precio_total

tipo_habitacion = input("Inserte el tipo de habitación (individual o doble): ")
vistas_mar = input("Inserte si quiere vistas al mar (si o no): ")
dias = int(input("Inserte cuantos dias quiere estar en el hotel: "))

precio_total = round(calculo(tipo_habitacion, vistas_mar, dias), 2)

print(f"Usted tiene que pagar: {precio_total}€")