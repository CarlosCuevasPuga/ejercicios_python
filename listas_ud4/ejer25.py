tareas = ["Comprar fruta", "Estudiar programación", "Desinstalar el LOL"]

while True:
    print("Bienvenido a la app de listas to-do más avanzada del universo")
    print("1. Ver tareas pendientes")
    print("2. Agregar tarea")
    print("0. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "0":
        break
    if opcion == "1":
        if len(tareas) > 0:
            print("------------------------")
            print("LISTA TAREAS PENDIENTES: ")
            for i, tarea in enumerate(tareas):
                print(f"{i+1}. {tarea}")
            n_tarea = int(input("Has completado algúna tarea? "))
            if n_tarea > 0 and n_tarea < len(tareas) + 1:
                tareas.pop(n_tarea - 1)
                print("!Eres un crack!")
            elif n_tarea < len(tareas) + 1:
                print("Tarea no valida")
        else:
            print("No hay tareas pendientes")
    elif opcion == "2":
        agregarTarea = input("¿Qué tarea quieres insertar? ")
        posicionLista = int(input("¿En que posicion la quieres agregar?"))
        while posicionLista < 1:
            posicionLista = int(input("[ERROR] Usted a introducido un número no valido, introduzcalo otra vez:"))
        tareas.insert(posicionLista - 1, agregarTarea)
        print(tareas)