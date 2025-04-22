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
            coleccion_str += f"[{i+1}] {consola.nombre} - Desarrollador/es: {consola.desarrollador} - Almacenamiento: {consola.almacenamiento}MB - Edicion Limitada: {consola.edicion_limitada_str()}\n"

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
        consola_a_mostrar = self.coleccion_consolas[pos+1]
        for atributos in consola_a_mostrar:
            print(atributos)

    def consola_seleccionada(self, pos) -> object:
        pos = abs(pos)
        consola_seleccionada = self.coleccion_consolas[pos-1]
        return consola_seleccionada

    def ordenar_por_fecha(self) -> list:
        fechas = [consola.fecha_salida for consola in self.coleccion_consolas]
        fechas.sort()
        fechas_ordenadas = []
        for fecha in fechas:
            for consola in self.coleccion_consolas:
                if consola.fecha_salida == fecha:
                    fechas_ordenadas.append(consola)

        return fechas_ordenadas