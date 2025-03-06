año=int(input("Inserta un año: "))
if año % 100 == 0:
    siglo=año // 100
    print(f"El año {año} es el siglo {siglo}")
else:
    siglo=año // 100 + 1
    print(f"El año {año} es el siglo {siglo}")
