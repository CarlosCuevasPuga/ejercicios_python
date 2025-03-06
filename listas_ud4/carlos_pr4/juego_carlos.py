import funciones

vidas = 10
nivel = 1
lista_palabras = [
  ["LUNA", "ALMA", "GATO"],
  ["MONEDA", "MADERA", "CEREAL"],
  ["ELEFANTE", "AVIONETA", "CANGURO"]
]
lista_insertadas = []
lista_letras = []

while True:
    if vidas == 0:
        break
    elif nivel == 4:
        print("Has ganado!!!")
        break

    if nivel == 1:
        palabra_aleatoria = funciones.elegir_palabra_aleatoria(lista_palabras[0])
    elif nivel == 2:
        palabra_aleatoria = funciones.elegir_palabra_aleatoria(lista_palabras[1])
    elif nivel == 3:
        palabra_aleatoria = funciones.elegir_palabra_aleatoria(lista_palabras[2])

    lista_insertadas = []
    lista_juego = []
    lista_letras = []
    for letra in palabra_aleatoria:
        lista_juego.append('_')
        lista_letras.append(letra)
    funciones.imprimir_menu(vidas, nivel)

    while vidas > 0:
        if lista_letras == lista_juego:
            print(f"Enhorabuena has encontrado la palabra:")
            print(lista_juego)
            nivel += 1
            break
        print("Palabra que tienes que encontrar:")
        print(lista_juego)
        letra_usuario = input("Inserta una letra: ").upper()

        # Comprueba que la letra inserta es valida
        letra = funciones.comprobar_letra(palabra_aleatoria, lista_letras, letra_usuario)
        insertada = funciones.comprobar_letra_repetida(lista_insertadas, letra_usuario)
        if insertada == True:
                print("Esa letra ya la has puesto")
        elif letra == letra_usuario:
                for i, letra in enumerate(lista_letras):
                    if lista_letras[i] == letra_usuario:
                        lista_juego[i] = letra_usuario
                        lista_insertadas.append(letra_usuario)
                print("Has encontrado una letra!!!, te sumo una vida")
                vidas += 1
        elif letra != letra_usuario:
            print("Has fallado :(, te resto 1 vida")
            vidas -= 1
        print(f"Tienes {vidas} vidas")