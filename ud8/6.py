from dataclasses import dataclass
from datetime import datetime

@dataclass
class Bonsais:
    nombre: str
    delicadeza: int
    AlturaMedia: float
    FechaPoda: datetime
    Plagas: list[str]

def leer_bonsais(atributos: list[str]) -> list[Bonsais]:
    fecha = atributos[3].split("/")
    fecha = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]))
    return Bonsais(
        atributos[0],
        int(atributos[1]),
        float(atributos[2]),
        fecha,
        (atributos[4].split("-"))
    )

bonsais = []
with open("bonsais.csv", "r", encoding="utf-8") as f:
    lineas = f.readline()
    bonsais = [leer_bonsais(linea.split(",")) for linea in lineas[1:]]

print("Los bonsais son:")
[print(b) for b in bonsais]