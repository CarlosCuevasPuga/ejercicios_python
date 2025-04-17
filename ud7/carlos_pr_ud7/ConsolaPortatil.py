from Consola import Consola
from datetime import datetime

class ConsolaPortatil(Consola):
    def __init__(self, nombre: str, desarrollador: list, fecha_salida: datetime, colores: list, edicion_limitada: bool, almacenamiento: int, autonomia: int):
        super().__init__(nombre, desarrollador, fecha_salida)

        self.colores = colores

        if edicion_limitada == True or edicion_limitada == False:
            self.edicion_limitada = edicion_limitada
        else:
            edicion_limitada = False

        if almacenamiento > 0:
            self.almacenamiento = almacenamiento
        else:
            self.almacenamiento = 100

        self.autonomia = autonomia

    def __str__(self) -> str:
        return super().__str__() + (
            f"Colores: {self.colores}, "
            f"Edicion Limitada {self.edicion_limitada_str()}"
        )

    def edicion_limitada_str(self) -> str:
        Edicion_limitada = "No"
        if Edicion_limitada == True:
            Edicion_limitada = "Si"
        return Edicion_limitada

    def clasificar_autonomia(self) -> str:
        if self.autonomia < 50:
            return "bajo"
        elif self.autonomia < 150:
            return "medio"
        else:
            return "alto"