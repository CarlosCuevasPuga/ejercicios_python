def menu():
    print("1. Perímetro triángulo")
    print("2. Área triángulo")
    print("3. Perímetro rectángulo")
    print("4. Área rectángulo")
    print("5. Es rectángulo cuadrado?")
    print("0. Salir")


def perimetro_triangulo(lado1: float, lado2: float, lado3: float) -> bool:
    perimetro_triangulo = False
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        perimetro_triangulo = True
    return perimetro_triangulo


while True:
    menu()
    opcion = input("Elige una opción: ")
    if opcion == "0":
        break
    elif opcion == "1":
        try:
            lado1 = float(input("Inserta el primer lado: "))
            lado2 = float(input("Inserta el segundo lado: "))
            lado3 = float(input("Inserta el tercer lado: "))
        except ValueError as error:
            print(f"Se ha producido un error:{error}")
        else:
            if perimetro_triangulo(lado1, lado2, lado3):
                perimetro = lado1 + lado2 + lado3
                print(f"El perímetro es: {perimetro}")
            else:
                print("Los lados insertados no forman un triángulo")
    elif opcion == "2":
        try:
            base = float(input("Inserta la base: "))
            altura = float(input("Inserta la altura: "))
        except ValueError as error:
            print(f"Se ha producido un error:{error}")
        else:
            area_triangulo = base * altura / 2
            print(f"El area de un triángulo es {area_triangulo}")
    elif opcion == "3":
        try:
            base = float(input("Inserta la base: "))
            altura = float(input("Inserta la altura: "))
        except ValueError as error:
            print(f"Se ha producido un error:{error}")
        else:
            perimetro_rectangulo = 2*base + 2*altura
            print(f"El perimetro de un rectangulo es {perimetro_rectangulo}")
    elif opcion == "4":
        try:
            base = float(input("Inserta la base: "))
            altura = float(input("Inserta la altura: "))
        except ValueError as error:
            print(f"Se ha producido un error:{error}")
        else:
            area_rectangulo = base * altura
            print(f"El area de un rectangulo es {area_rectangulo}")
    elif opcion == "5":
        try:
            base = float(input("Inserta la base: "))
            altura = float(input("Inserta la altura: "))
        except ValueError as error:
            print(f"Se ha producido un error:{error}")
        else:
            if base == altura:
                print("Es un cuadrado")
            else:
                print("Es un rectángulo")
    else:
        print("Opción no valida")
