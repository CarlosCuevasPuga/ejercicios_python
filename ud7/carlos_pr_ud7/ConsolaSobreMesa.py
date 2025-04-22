from Consola import Consola
from datetime import datetime

class ConsolaSobreMesa(Consola):
    def __init__(self, nombre: str, desarrollador: list, fecha_salida: datetime, colores: list, edicion_limitada: bool, almacenamiento: int, num_usb: int):
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

        self.num_usb = num_usb

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

    def filtrar_colores(self, color1: str, color2: str):
        return color1 in self.colores and color2 in self.colores