from Planeta import Planeta

planetas = [
    Planeta("Mercurio", True, 0),
    Planeta("Venus", True, 0),
    Planeta("Tierra", True, 1),
    Planeta("Marte", True, 2),
    Planeta("Júpiter", False, 95),
    Planeta("Saturno", False, 146),
    Planeta("Urano", False, 27),
    Planeta("Neptuno", False, 14),
    Planeta("Plutón", True, 5)
]

for planeta in planetas:
    print(f"\n{planeta}\n")

planetas_rocosos_sin_luna= [planeta for planeta in planetas if planeta.rocoso == True and planeta.num_lunas == 0]

print("\n--------------------------------\n")

for planeta in planetas_rocosos_sin_luna:
    print(f"\n{planeta}\n")