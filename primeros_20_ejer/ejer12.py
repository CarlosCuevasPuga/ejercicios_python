calificacion=int(input("Escriba su calificación: "))

if calificacion>=90 and calificacion<=100:
    print("Usted tiene una A")
elif calificacion>=80 and calificacion<=89:
    print("Usted tiene una B")
elif calificacion>=70 and calificacion<=79:
    print("Usted tiene una C")
elif calificacion>=60 and calificacion<=69:
    print("Usted tiene una D")
else:
    print("Usted tiene una F")