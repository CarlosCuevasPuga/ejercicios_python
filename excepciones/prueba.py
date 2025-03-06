def CalculoAreaTriangulo (base: int, altura: int) -> int:
    
    AreaTriangulo = (base * altura) / 2

    return AreaTriangulo

while True:
    try:
        base = int(input("Introduzca la base: "))
        altura = int(input("Introduzca la altura: "))

        print(f"El area de un trinagulo es: {CalculoAreaTriangulo(base, altura)}")
        break

    except ValueError as ex_num_neg:
        print(f"[ERROR]: Uno de los valores introducidos no es un número: {ex_num_neg}")