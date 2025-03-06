import random

nVeces = 10

def operadorAleatorio() -> str:
    codigo = random.randint(1,3)
    if codigo == 1:
        operador = "+"
    elif codigo == 2:
        operador = "-"
    elif codigo == 3:
        operador = "*"
    return operador

def operacion(inicio: int, final: int) -> int:
    operacion1 = random.randint(inicio,final)
    operacion2 = random.randint(inicio,final)
    operador = operadorAleatorio()
    if operador == "+":
        resultado = operacion1 + operacion2
    elif operador == "-":
        resultado = operacion1 - operacion2
    elif operador == "*":
        resultado = operacion1 * operacion2
    
    print(f"{operacion1} {operador} {operacion2}")

    return resultado

for i in range(nVeces):
    resultado = operacion(1,10)
    resultadoUsuario = int(input("Resuelve: "))
    if resultadoUsuario == resultado:
        print("Has acertado")
    else:
        print("Has fallado")