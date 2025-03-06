usuario = input("Inserta un nombre de usuario: ")
contraseña1 = input("Inserta la contraseña: ")
contraseña2 = input("Inserta otra vez la contraseña: ")

while contraseña1 != contraseña2:
    print("Las contraseñas no coinciden, vuelva a introducirlas")
    contraseña1 = input("Inserta la contraseña: ")
    contraseña2 = input("Inserta otra vez la contraseña: ")
input(f"!!!Bienvenido señor {usuario}!!!")