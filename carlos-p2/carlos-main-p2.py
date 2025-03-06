import funcs


numMin = 0
numMax = 10
vidas = 3
opcion_vidas = 3
partida = 0
cuentas_generadas = 0
racha_aciertos = 0
racha_usuario = 0
preguntas_correctas = 0
preguntas_incorrectas = 0
total_correctas = 0
total_incorrectas = 0
trofeo_bronce = False
trofeo_plata = False
trofeo_oro = False
trofeo_superviviente = False
trofeo_calculatron = False

while True:
    opcion = funcs.imprimirMenu()
    if opcion == 0:
        break
    elif opcion == 1:

        vidas = opcion_vidas
        preguntas_correctas = 0
        preguntas_incorrectas = 0
        partida = partida + 1
        racha_aciertos = 0

        while vidas != 0:
            resultado = funcs.generarCuenta(numMin,numMax)
            resultado_usuario = int(input("Resuelve: "))
            cuentas_generadas = cuentas_generadas + 1
            if resultado_usuario == resultado:
                print("Correcto !")

                preguntas_correctas = preguntas_correctas + 1
                total_correctas = total_correctas + 1
                racha_aciertos = racha_aciertos + 1
                racha_usuario = racha_aciertos
 
                if racha_aciertos > racha_usuario:
                    racha_usuario = racha_aciertos
                
                if racha_aciertos == 3 and trofeo_bronce == False:
                    print("LOGRO DE BRONCE DESBLOQUEADO")
                    trofeo_bronce = True
                if racha_aciertos == 7 and trofeo_plata == False:
                    print("LOGRO DE PLATA DESBLOQUEADO")
                    trofeo_plata = True
                if racha_aciertos == 10 and trofeo_oro == False:
                    print("LOGRO DE ORO DESBLOQUEADO")
                    trofeo_oro = True
                if racha_aciertos == 10 and vidas == 1 and trofeo_superviviente == False:
                    print("LOGRO DE VALIENTE DESBLOQUEADO")
                    trofeo_superviviente = True
                if trofeo_bronce == True and trofeo_plata == True and trofeo_oro == True and trofeo_superviviente == True:
                    print("LOGRO CALCULATRÓN DESBLOQUEADO")
                    trofeo_calculatron = True

            elif resultado_usuario != resultado:
                print(f"Incorrecto, el resultado era {resultado}")
                vidas = vidas - 1
                preguntas_incorrectas = preguntas_incorrectas + 1
                total_incorrectas = total_incorrectas + 1
                racha_aciertos = 0
                print(f"te quedan {vidas} vidas")

        print(f"En tu partida número {partida} has acertado {preguntas_correctas} y has fallado {preguntas_incorrectas}")
        print(f"Has acertado un {round((preguntas_correctas / cuentas_generadas) * 100, 2)}% de las cuentas")

    elif opcion == 2:
            
        opcion_config = 1
        while opcion_config != 0:
            print("La configuración actual es: ")
            print(f"Número de vidas: {opcion_vidas}")
            print(f"Número mínimo: {numMin}")
            print(f"Número máximo: {numMax}")
            print("1. cambiar número de vidas")
            print("2. cambiar número mínimo")
            print("3. cambiar número máximo")
            print("0. salir")
            opcion_config = int(input("Elija una opción: "))

            if opcion_config == 1:
                opcion_vidas = funcs.config1()
            elif opcion_config == 2:
                numMin = funcs.config2(numMax)
            elif opcion_config == 3:
                numMax = funcs.config3(numMin)

    elif opcion == 3:

        funcs.estadisticas(partida, cuentas_generadas, total_correctas, total_incorrectas, racha_usuario)

    elif opcion == 4:

        print(f"Logro de bronce: acierta tres operaciones consecutivas en una misma partida -> {"SI" if trofeo_bronce == True else "NO"} obtenido")
        print(f"Logro de plata: acierta siete operaciones consecutivas en una misma partida -> {"SI" if trofeo_plata == True else "NO"} obtenido")
        print(f"Logro de oro: acierta diez operaciones consecutivas en una misma partida -> {"SI" if trofeo_oro == True else "NO"} obtenido")
        print(f"Logro de valiente: resuelve 10 ecuaciones seguidas con 1 vida -> {"SI" if trofeo_superviviente == True else "NO"} obtenido")
        print(f"Logro Calculatron: consigue todos los trofeos -> {"SI" if trofeo_calculatron == True else "NO"} obtenido")