from Videojuego import Videojuego
from Usuario import Usuario
from datos import get_juegos
from datos import get_usuarios
import funcs

lista_nombres_usuarios = [usuario.nombre for usuario in get_usuarios()]
lista_contraseñas_usuarios = [usuario.contra for usuario in get_usuarios()]
lista_juegos_usuario = []
login_completado = False
saldo_ingresado = 0

nombre_usuario = input("Login: ")
while True:
    if nombre_usuario in lista_nombres_usuarios:
        contraseña = input("contraseña: ")
        if contraseña in lista_contraseñas_usuarios:
            login_completado = True
            while login_completado:
                saldo_usuario = funcs.saldo_usuario(nombre_usuario)
                saldo_usuario += saldo_ingresado
                lista_videojuegos = funcs.videojuegos_segun_edad(nombre_usuario)
                for i, juego in enumerate(lista_videojuegos):
                    print(f"[{i+1}]. {juego.nombre}")    
                print("\n----------------------\n")
                print(f"Actualmente tienes {saldo_usuario}")
                print("\n----------------------\n")
                print("[V]er mis juegos")
                print("[I]ngresar dinero")
                print("Ir al [c]arrito")
                print("[S]alir")
                opcion = input("¿Qué quieres hacer?").lower()
                if opcion >= 1 and opcion <= len(lista_juegos_usuario):
                    juego_seleccionado = funcs.juego_seleccionado(nombre_usuario, opcion)
                    print(juego_seleccionado)
                elif opcion == "v":
                    print("Tienes los siguientes juegos:")
                    for juego in lista_juegos_usuario:
                        print(juego)
                elif opcion == "i":
                    saldo_ingresado = int(input("Cantidad a ingresar: "))
                    print(f"Enhorabuena has ingresado {saldo_ingresado} €")
        else:
            while not contraseña in lista_contraseñas_usuarios:
                contraseña = input("contraseña incorrecta, inserte de nuevo la contrasela: ")
    else:
        while not nombre_usuario in lista_nombres_usuarios:
            print("El nombre de usuario no existe")
            nombre_usuario = input("Inserte de nuevo el nombre: ")