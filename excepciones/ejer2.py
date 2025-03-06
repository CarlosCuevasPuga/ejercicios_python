opcion = 0
grados = 0

while True:
    try:
        print("Introduzca a que temperatura quiere pasar los grados: ")
        print("1. Fharenheit")
        print("2. Celsius")
        opcion = int(input("Inserte su elección: "))
        grados = float(input("Introduzca los grados a calcular: "))
    except ValueError as error:
        print(f"Usted a introducido un tipo de dato no valido {error}")
    else:
        if opcion == 1:
            calculo_a_celsius = (grados - 32)*5/9
            print(f"Es: {calculo_a_celsius}")
        elif opcion == 2:
            calculo_a_fharenheit = (grados * 9 / 5)+32
            print(f"Es: {calculo_a_fharenheit}")
