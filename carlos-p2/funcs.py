import random

def operadorAleatorio() -> str:
    codigo = random.randint(1,3)
    if codigo == 1:
        operador = "+"
    elif codigo == 2:
        operador = "-"
    elif codigo == 3:
        operador = "*"

    return operador

def generarCuenta(numMin: int, numMax: int) -> int:
    operacion1 = random.randint(numMin,numMax)
    operacion2 = random.randint(numMin,numMax)
    operador = operadorAleatorio()
    if operador == "+":
        resultado = operacion1 + operacion2
    elif operador == "-":
        resultado = operacion1 - operacion2
    elif operador == "*":
        resultado = operacion1 * operacion2
    
    print(f"{operacion1} {operador} {operacion2} = ")

    return resultado

def imprimirMenu() -> int:
    print("Bienvenido al Calculatrón 2.0 !!!")
    print("1. Jugar")
    print("2. Configuración")
    print("3. Estadísticas")
    print("4. Logros")
    print("0. Salir")
    opcion = int(input("Selecciona una opción: "))

    return opcion

def config1() -> int:
    opcion_config = 1

    if opcion_config == 1:
        opcion_vidas = int(input("Inserta el número de vidas (Entre 1 y 10): "))
        while True:
            if opcion_vidas < 1 or opcion_vidas > 10:
                opcion_vidas = int(input("Número no válido, ha de ser entre 1 y 10: "))
            elif opcion_vidas >= 1 or opcion_vidas <= 10:
                break

    return opcion_vidas

def config2(numMax: int) -> int:

    nuevoMinimo = int(input("Nuevo mínimo: "))
    while True:
        if nuevoMinimo > numMax:
            nuevoMinimo = int(input("El número minimo ha de ser menor al número máximo: "))
        elif nuevoMinimo <= numMax:
            numMin = nuevoMinimo
            break

    return numMin

def config3(numMin: int) -> int:

    nuevoMaximo = int(input("Nuevo máximo: "))
    while True:
        if nuevoMaximo < numMin:
            nuevoMaximo = int(input("El número máximo ha de ser mayor al número minimo: "))
        elif nuevoMaximo >= numMin:
            numMax = nuevoMaximo
            break

    return numMax

def estadisticas(partida: int, cuentas_generadas: int, total_correctas: int, total_incorrectas: int, racha_usuario: int):

    porcentaje_correctas = round((total_correctas / cuentas_generadas) * 100, 2)
    porcentaje_incorrectas = round((total_incorrectas / cuentas_generadas) * 100, 2)

    print(f"Has jugado un total de {partida} partidas")
    print(f"Habiendo realizado un total de {cuentas_generadas} cuentas")
    print(f"Has acertado un total de {total_correctas}")
    print(f"Tu porcentaje de acierto es de {porcentaje_correctas}%")
    print(f"Has fallado un total de {total_incorrectas} operaciones")
    print(f"Tu porcentaje de fallos es del {porcentaje_incorrectas}%")
    print(f"Tu maxima racha de aciertos es {racha_usuario}")