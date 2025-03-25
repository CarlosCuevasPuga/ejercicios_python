from Videojuego import Videojuego
from Usuario import Usuario
from datos import get_juegos
from datos import get_usuarios
import funcs

lista_nombres_usuarios = [usuario.nombre for usuario in get_usuarios()]
lista_contraseñas_usuarios = [usuario.contra for usuario in get_usuarios()]
lista_juegos_usuario = []
lista_carrito = []
login_completado = False
intentos_contra = 3

# Control del login del usuario
nombre_usuario = input("Login: ")
while not login_completado and intentos_contra > 0:
    if nombre_usuario in lista_nombres_usuarios:
        contraseña = input("contraseña: ")
        if contraseña in lista_contraseñas_usuarios:
            # Parametros necesarios para que el programa funcione correctamente
            login_completado = True
            lista_videojuegos = funcs.videojuegos_segun_edad(nombre_usuario)
            saldo_usuario = float(funcs.saldo_usuario(nombre_usuario))
            # Bucle que se ejecuta cuando el usuario a completado el login
            while login_completado:
                #Imprime el menu del programa
                print("JUEGOS DISPONIBLES PARA COMPRAR:")
                for i, juego in enumerate(lista_videojuegos):
                    print(f"[{i+1}]. {juego.nombre}, precio: {juego.precio_base}€")
                print("\n----------------------\n")
                print(f"Actualmente tienes {round(saldo_usuario,2)}€")
                print("\n----------------------\n")
                print("[V]er mis juegos")
                print("[I]ngresar dinero")
                print("Ir al [c]arrito")
                print("[S]alir")
                opcion = input("¿Qué quieres hacer? ").lower()
                # Control de todas las opciones disponibles del usuario
                if opcion == "s":
                    break
                elif opcion == "v":
                    if len(lista_juegos_usuario) <= 0:
                        print("No tienes ningun juego")
                        input()
                    else:
                        print("Tienes los siguientes juegos:")
                        for juego in lista_juegos_usuario:
                            print(juego.nombre)
                        input()
                elif opcion == "i":
                    saldo_ingresado = round(float(input("Cantidad a ingresar: ")),2)
                    if saldo_ingresado >= 0:
                        print(f"Enhorabuena has ingresado {saldo_ingresado} €")
                        saldo_usuario += saldo_ingresado
                    else:
                        print("[ERROR] Solo se permite ingresar una cantidad positiva de dinero")
                    input()
                elif opcion == "c":
                    if len(lista_carrito) <= 0:
                        print("No hay juegos en el carrito")
                        input()
                    else:
                        precio_total = 0
                        print("Tienes los siguientes juegos en el carrito:")
                        for juego in lista_carrito:
                            print(f"{juego.nombre} -- precio: {juego.precio_base}")
                            precio_total += juego.precio_base
                        print(f"el precio total es: {precio_total}€")
                        print("[P]agar")
                        print("[V]olver")
                        opcion_carrito = input().lower()
                        if opcion_carrito == "p" and saldo_usuario >= precio_total:
                            for juego in lista_carrito:
                                lista_juegos_usuario.append(juego)
                            lista_carrito.clear()
                            print("Pago realizado con exito")
                            saldo_usuario -= precio_total
                            input()
                        elif opcion_carrito == "p" and saldo_usuario < precio_total:
                            print("Saldo insuficiente")
                            input()
                else:
                    # convierte la opcion en entero y imprime el juego seleccionado
                    opcion = funcs.convertir_a_entero(opcion)
                    print(lista_videojuegos[opcion-1])
                    juego_elegido = input("¿Quieres añadir el juego al carrito (S/N)? ").lower()
                    if juego_elegido == "s":
                        lista_carrito.append(lista_videojuegos[opcion-1])
                        lista_videojuegos.remove(lista_videojuegos[opcion-1])
        else:
            intentos_contra -= 1
            while not contraseña in lista_contraseñas_usuarios:
                contraseña = input("contraseña incorrecta, inserte de nuevo la contrasela: ")
                intentos_contra -= 1
                if intentos_contra == 0:
                    break
    else:
        while not nombre_usuario in lista_nombres_usuarios:
            print("El nombre de usuario no existe")
            nombre_usuario = input("Inserte de nuevo el nombre: ")