tareas = ["Comprar fruta", "Estudiar programación", "Desinstalar el LOL"]

print("Bienvenido a la app to-do")
print("1. Ver tareas pendientes")
print("2. Agregar tarea")
print("0. Salir")

while True:
    opcion = input("Elige una opción: ")
    if opcion == "0":
        break
    if opcion == "1":
        print("Tareas pendientes: ")
        for i, tarea in enumerate(tareas):
            print(f"{i+1}. {tarea}")
    elif opcion == "2":
        agregarTarea = input("¿Qué tarea quieres insertar? ")
        posicionLista = int(input("¿En que posicion la quieres agregar?"))
        while posicionLista < 1:
            posicionLista = int(input("[ERROR] Usted a introducido un número no valido, introduzcalo otra vez:"))
        tareas.insert(posicionLista - 1, agregarTarea)
        print(tareas)
