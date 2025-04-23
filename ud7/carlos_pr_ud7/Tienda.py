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
        consola_a_mostrar = self.coleccion_consolas[pos-1]
        # Muestro solo los atributos que comparten las 2 listas
        fecha = consola_a_mostrar.fecha_salida.strftime("%d/%m/%Y")
        return(
            "\nDatos de la consola:\n"
            f"[1]] Nombre: {consola_a_mostrar.nombre}\n"
            f"[2] Desarrollador/es: {consola_a_mostrar.desarrollador}\n"
            f"[3] Fecha de lanzamiento: {fecha}\n"
            f"[4] Colores: {consola_a_mostrar.colores}\n"
            f"[5] Edicion Limitada: {consola_a_mostrar.edicion_limitada}\n"
            f"[6] Almacenamiento: {consola_a_mostrar.almacenamiento}"
        )

    def consola_seleccionada_a_borrar(self, pos) -> object:
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
        fechas_ordenadas.reverse()
        return fechas_ordenadas