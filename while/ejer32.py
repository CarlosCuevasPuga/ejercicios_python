num = int(input("¿Cuántos terminos quieres? "))
i = 1

while i <= num:
    if i == 1:
        termino1 = 0
        print(termino1)
    if i == 2:
        termino2 = 1
        print(termino2)
    if i >= 3:
        termino3 = termino1 + termino2
        print(termino3)
        termino1 = termino2
        termino2 = termino3
    i = i + 1