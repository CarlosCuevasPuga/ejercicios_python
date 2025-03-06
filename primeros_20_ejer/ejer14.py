temperatura=int(input("Ingrese la temperatura: "))
escala=input("Ingrese su escala original (Celsius o Farhenheit): ")

if escala=="Celsius":
    input(f"La temperatura en Farhenheit es: {(temperatura * 9) / 5 + 32} Farhenheits")
else:
    input(f"La temperatura en Celsius es: {(temperatura - 32) * 5 / 9 } Celsius")