num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))
operacion=input("Introduce la operación que quieres hacer (Sumar, Restar, Multiplicar y Dividir): ")

if operacion=="Sumar":
    print(f"La suma entre el número {num1} y {num2} es {num1 + num2}")
elif operacion=="Restar":
    print(f"La resta entre el número {num1} y {num2} es {num1 - num2}")
elif operacion=="Multiplicar":
    print(f"La multiplicacion entre el número {num1} y {num2} es {num1 * num2}")
else:
    print(f"La division entre el número {num1} y {num2} es {num1/num2}")