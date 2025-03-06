while True:
    
    precio = float(input("Introduzca el precio base de su producto: "))

    if precio < 0:
        break   
    
    iva = int(input("Introduzca el IVA que se le aplica: "))

    impuesto = (precio * iva) / 100
    precio_final = round(precio + impuesto,2)
    print(f"El impuesto es {round(impuesto,2)} y el precio final es {round(precio_final,2)}")

