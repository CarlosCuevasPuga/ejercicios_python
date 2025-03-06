# Pedimos al usuario cuántos números va a introducir
n = int(input("¿Cuántos números vas a introducir? "))

# Inicializamos las variables con 0, que funcionará solo si los números ingresados son positivos
primer_mayor = 0
segundo_mayor = 0
tercer_mayor = 0

# Leemos n números
for i in range(n):
    num = int(input(f"Introduce el número {i + 1}: "))

    # Actualizamos las variables para mantener los 3 mayores números
    if num > primer_mayor:
        tercer_mayor = segundo_mayor
        segundo_mayor = primer_mayor
        primer_mayor = num
    elif num > segundo_mayor:
        tercer_mayor = segundo_mayor
        segundo_mayor = num
    elif num > tercer_mayor:
        tercer_mayor = num

# Imprimimos los números ordenados de mayor a menor
print("Los números ordenados de mayor a menor son:")
print(primer_mayor)
print(segundo_mayor)
print(tercer_mayor)