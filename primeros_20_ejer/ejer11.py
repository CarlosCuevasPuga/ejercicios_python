edad=int(input("¿Cuantos años tienes?: "))

if edad>=0 and edad<=2:
    print("Eres un Bebe")
elif edad>=3 and edad<=12:
    print("Eres un Niño/a")
elif edad>=13 and edad<=17:
    print("Eres un adolescente")
elif edad>=18 and edad<=34:
    print("Eres un adulto pero no")
elif edad==35:
    print("La mejor edad posible")
elif edad>=36 and edad<=50:
    print("Eres un adulto")
elif edad>=51 and edad<=67:
    print("Eres un pre-anciano")
elif edad>=68 and edad<=99:
    print("Eres un anciano")
else:
    print("Eres un centenario")