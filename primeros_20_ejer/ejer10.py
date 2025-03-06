peso=float(input("Escribe el peso de tu coche(Kg): "))

if peso<1000:
    print("Su coche tiene un peso ligero")
elif peso>=1000 and peso<2000:
    print("Su coche tiene un peso medio")
else:
    print("Su coche tiene un peso pesado")