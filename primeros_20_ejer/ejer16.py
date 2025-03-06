lado1=float(input("Ingrese el primer lado del triangulo:"))
lado2=float(input("Ingrese el segundo lado del triangulo:"))
lado3=float(input("Ingrese el tercer lado del triangulo:"))

if lado1==lado2 and lado1==lado3 and lado2==lado1 and lado2==lado3 and lado3==lado1 and lado3==lado2:
    print("El triangulo es equilátero")
elif lado1==lado2 and lado1!=lado3 or lado1==lado3 and lado1!=lado2 or lado2==lado1 and lado2!=lado3 or lado2==lado3 and lado2!=lado1 or lado3==lado1 and lado3!=lado2 or lado3==lado2 and lado3!=lado1:
    print("El triangulo es isósceles")
else:
    print("El triangulo es escaleno")