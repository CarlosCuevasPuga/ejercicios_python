from ConsolaPortatil import ConsolaPortatil
from ConsolaSobreMesa import ConsolaSobreMesa
from datetime import datetime

class Tienda:
    
    def __init__(self):
        self.coleccion_consolas = []

    def meter_consolas_sobremesa(self, consola: ConsolaSobreMesa):
        self.coleccion_consolas.append(consola)

    def meter_consolas_portatil(self, consola: ConsolaPortatil):
        self.coleccion_consolas.append(consola)

    def __str__(self) -> str:
        coleccion_str = "\nCONSOLAS DISPONIBLES:\n\n"
        for i, consola in enumerate(self.coleccion_consolas):
            coleccion_str += f"[{i+1}] {consola.nombre} - Almacenamiento: {consola.almacenamiento}MB - Edicion Limitada: {consola.edicion_limitada_str()}\n"

        return coleccion_str

    def insertar(self, objeto):
        pass

    def borrar(self, pos):
        pos = abs(pos)
        for i, consola in enumerate(self.coleccion_consolas):
            i += 1
            if i == pos:
                return self.coleccion_consolas.remove(consola)

    def mostrar(self, pos) -> object:
        pos = abs(pos)
        for i, consola in enumerate(self.coleccion_consolas):
            i += 1
            if i == pos:
                return consola
    def ordenar_por_fecha(self):
        consolas_por_fecha = [consola for consola in self.coleccion_consolas]
        return self.coleccion_consolas