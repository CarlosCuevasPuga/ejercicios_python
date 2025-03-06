dia = input("Inserta el dia de la semana (L, M, X, J, V, S, D): ")
hora = int(input("Inserta la hora en la que te subes al taxi: "))
kms = float(input("Inserta el número de kms: "))

if dia == "S":
    if hora >= 8 and hora<= 18:
        tarifa = 1.2
    else:
        tarifa = 1.5
elif dia == "D":
    tarifa = 1.5
else:
    if hora >= 8 and hora <= 18:
        tarifa = 1
    elif hora >= 19 and hora < 23:
        tarifa = 1.2
    elif hora == 23 or hora >= 0 and hora <= 7:
        tarifa = 1.5

tarifa = 3.5 + (tarifa * kms)

print(f"Coges el taxi el dia {dia} y a la hora {hora} y haces {kms}, el viaje te costaria {tarifa}")