from EjemplarVideojuego import EjemplarVideojuego

class ColeccionVideojuegos:
    def __init__(self):
        self.videojuegos = []
    # Lo tengo que hacer de esta manera por culpa de la version de python que tengo
    def meter_videojuegos(self, juego: EjemplarVideojuego):
        self.videojuegos.append(juego)

    def __str__(self) -> str:
        coleccion_str = "CATALOGO COMPLETO: \n"
        for videojuego in self.videojuegos:
            coleccion_str += f"Nombre: {videojuego.nombre} - Estado: {videojuego.estado_str()}\n"
        return coleccion_str

    def juegos_repetidos(self) -> list:
        no_repetidos = []
        repetidos = []
        for juego in self.videojuegos:
            if [juego.nombre, juego.fecha_salida] not in no_repetidos:
                no_repetidos.append([juego.nombre, juego.fecha_salida])
            else:
                if juego not in repetidos:
                    repetidos.append(juego)
                    
        return repetidos

    def mostrar_juegos_repetidos(self):
        repetidos = self.juegos_repetidos()
        if repetidos:
            for juego in repetidos:
                print(f"Juego repetido: {juego}")

    def eliminar_juego(self, id: int):
        self.videojuegos = [juego for juego in self.videojuegos if juego.id != id]