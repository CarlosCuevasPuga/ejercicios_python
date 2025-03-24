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

while not login_completado and intentos_contra > 0:
    nombre_usuario = input("Login: ")
    if nombre_usuario in lista_nombres_usuarios:
        contraseña = input("contraseña: ")
        if contraseña in lista_contraseñas_usuarios:
            login_completado = True
            lista_videojuegos = funcs.videojuegos_segun_edad(nombre_usuario)
            saldo_usuario = funcs.saldo_usuario(nombre_usuario)
            while login_completado:
                for i, juego in enumerate(lista_videojuegos):
                    print(f"[{i+1}]. {juego.nombre}")
                print("\n----------------------\n")
                print(f"Actualmente tienes {saldo_usuario}€")
                print("\n----------------------\n")
                print("[V]er mis juegos")
                print("[I]ngresar dinero")
                print("Ir al [c]arrito")
                print("[S]alir")
                opcion = input("¿Qué quieres hacer?").lower()
                if opcion == "s":
                    break
                elif opcion == "v":
                    if len(lista_juegos_usuario) <= 0:
                        print("No tienes ningun juego")
                    else:
                        print("Tienes los siguientes juegos:")
                        for juego in lista_juegos_usuario:
                            print(juego)
                elif opcion == "i":
                    saldo_ingresado = float(input("Cantidad a ingresar: "))
                    saldo_usuario = funcs.saldo_ingresado(saldo_usuario, saldo_ingresado)
                    print(f"Enhorabuena has ingresado {saldo_usuario} €")
                    input()
                elif opcion == "c":
                    print("Tienes los siguientes juegos en el carrito:")
                    if len(lista_carrito) <= 0:
                        print("No hay juegos en el carrito")
                        input()
                    else:
                        precio_total = 0
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
                            print("Pago realizado con exito")
                            saldo_usuario -= precio_total
                            input()
                        elif opcion_carrito == "p" and saldo_usuario < precio_total:
                            print("Saldo insuficiente")
                            input()
                else:
                    opcion = int(opcion)
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