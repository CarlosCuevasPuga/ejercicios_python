num = 0
num_veces = 0
primer_mayor = 0
segundo_mayor = 0
tercer_mayor = 0

n = int(input("Inserta la cantidad de veces que quieres introducir números: "))

while num_veces < n:
    num = int(input("Introduce un número: "))

    if num > primer_mayor:
        tercer_mayor = segundo_mayor
        segundo_mayor = primer_mayor
        primer_mayor = num
    elif num > segundo_mayor:
        tercer_mayor = segundo_mayor
        segundo_mayor = num
    elif num > tercer_mayor:
        tercer_mayor = num

    num_veces = num_veces + 1

print(primer_mayor)
print(segundo_mayor)
print(tercer_mayor)