from Consolas import Consola
from datetime import datetime

class ConsolaSobreMesa(Consola):
    def __init__(self, nombre: str, desarrollador: str, fecha_salida: datetime, colores: list, edicion_limitada: bool, num_mandos: int):
        super().__init__(nombre, desarrollador, fecha_salida)

        self.colores = colores
        self.edicion_limitada = edicion_limitada
        self.num_mandos = num_mandos

    def __str__(self) -> str:
        return super().__str__() + (
            f"Colores: {self.colores}, "
            f"Edicion limitada: {self.edicion_limitada_str()}"
        )

    def edicion_limitada_str(self) -> str:
        Edicion_limitada = "No"
        if Edicion_limitada == True:
            Edicion_limitada = "Si"
        return Edicion_limitada