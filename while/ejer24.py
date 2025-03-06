usuario = input("Introduzca su nombre de usuario: ")
contraseña1 = input("Introduzca su contraseña: ")
contraseña2 = input("Introduzca otra vez su contraseña: ")

while contraseña1 != contraseña2:
    print("Las contraseñas no conciden")
    contraseña1 = input("Introduzca su contraseña: ")
    contraseña2 = input("Introduzca otra vez su contraseña: ")
input(f"!!!Bienvenido señor {usuario}!!!")