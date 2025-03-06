num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))
operacion=input("Introduce la operación que quieres hacer (Sumar, Restar, Multiplicar y Dividir): ")

match operacion:
    case "Sumar":
        print(f"La suma entre el número {num1} y {num2} es {num1 + num2}")
    case "Restar":
        print(f"La resta entre el número {num1} y {num2} es {num1 - num2}")
    case "Multiplicar":
        print(f"La multiplicacion entre el número {num1} y {num2} es {num1 * num2}")
    case "Dividir":
        print(f"La division entre el número {num1} y {num2} es {num1/num2}")