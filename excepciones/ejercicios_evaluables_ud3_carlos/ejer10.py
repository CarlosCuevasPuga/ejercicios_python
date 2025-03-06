def calculo_num_intermedios(num_usuario1: int, num_usuario2: int):
    num_intermedios = 0
    i = 0
    while num_intermedios != num_usuario2 - 1:
        i += 1
        num_intermedios = num_usuario1 + i
        print(num_intermedios)

while True:
    try:
        num_usuario1 = int(input("Introduce el primer número: "))
        num_usuario2 = int(input("Introduce el segundo número: "))
    except ValueError as error:
        print(f"[ERROR] Ha introduucido un dato no valido {error}")
    except Exception as error:
        print(f"[ERROR] Ha ocurrido un error {error}")
    else:
        if num_usuario1 < num_usuario2:
            calculo_num_intermedios(num_usuario1, num_usuario2)
        else:
            print("[ERROR] El primer número tiene que ser menor que el segundo número")