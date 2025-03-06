num1 = 10
num2 = 30
total = num1 + num2

while True:

    respuesta = int(input(f"Resuelva la operacion: {num1} +  {num2}: "))
    if respuesta == total:
        print("Usted es Humano")
        break
    else:
        print("No es correcto, vuelva a intentarlo.")