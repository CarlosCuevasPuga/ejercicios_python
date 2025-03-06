while True:

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. División entera")
    print("6. Resto de 2 números")
    print("Para salir escriba fin")
 
    opcion = input("Elija una opción: ")

    if opcion == "fin":
        break

    num1 = int(input("Escriba el primer número: "))
    num2 = int(input("Escriba el segundo número: "))
    
    if opcion == "1":
        total = num1 + num2
        print(f"La suma de {num1} + {num2} es {total}")
    elif opcion == "2":
        total = num1 - num2
        print(f"La resta entre el {num1} - {num2} es {total}")
    elif opcion == "3":
        total = num1 * num2
        print(f"La multiplicación entre el {num1} x {num2} es {total}")
    elif opcion == "4":
        total = num1 / num2
        print(f"La división entre el {num1} / {num2} es {total}")
    elif opcion == "5":
        total = num1 // num2
        print(f"La división entera entre el {num1} / {num2} es {total}")
    elif opcion == "6":
        total = num1 % num2
        print(f"El resto entre el {num1} % {num2} es {total}")