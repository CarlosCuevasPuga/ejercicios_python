figura=input("Ingrese una figura geometrica (Triangulo, Rectangulo o Circunferencia): ")

if figura=="Triangulo":
    base=int(input("Ingrese la base: "))
    altura=int(input("Ingrese la altura: "))
    print(f"El area del triangulo es: {(base*altura)/2}") 
elif figura=="Rectangulo":
    base=int(input("Ingrese la base: "))
    altura=int(input("Ingrese la altura: "))
    print(f"El area del rectangulo es: {base*altura}") 
else:
    radio=int(input("Ingrese el radio: "))
    print(f"El area de la circunferencia es: {(3.14*radio**2)}") 