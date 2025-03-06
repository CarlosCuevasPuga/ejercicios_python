while True:
    nReal = float(input("Introduzca un número real: "))

    if nReal == 0:
        break
    
    entero = int(input("Introduzca un entero: "))
    redondeo = round(nReal,entero)
    print(f"El redondeo de ese número es {redondeo}")

