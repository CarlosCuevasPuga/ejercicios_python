lado1 = float(input("Inserta el primer lado: "))
lado2 = float(input("Inserta el segundo lado: "))
lado3 = float(input("Inserta el tercer lado: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 >lado2:
    print("El triangulo es válido")
else:
    print("El triangulo no es válido")