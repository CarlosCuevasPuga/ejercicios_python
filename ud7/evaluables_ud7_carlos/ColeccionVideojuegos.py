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
        
        def comparar(j1: EjemplarVideojuego, j2: EjemplarVideojuego) -> bool:
            return j1.nombre == j2.nombre and j1.fecha_salida == j2.fecha_salida
        
        def contiene(juego: EjemplarVideojuego, juegos: list) -> bool:
            lo_contiene = False
            for j in juegos:
                if comparar(juego, j):
                    lo_contiene = True
                    break
            return lo_contiene
        
        repetidos = []
        no_repetidos = []

        for j in self.coleccion:
            if not contiene(j, no_repetidos):
                no_repetidos.append(j)
            else:
                if not contiene(j, repetidos):
                    repetidos.append(j)
       
        return repetidos


    def mostrar_juegos_repetidos(self):
        repetidos = self.juegos_repetidos()

        if repetidos:
            print("Los juegos repetidos son: ")

            for juego in repetidos:
                print(juego.nombre)
        else:
            print("No hay juegos repetidos")

    def eliminar_juego(self, id: int):
        self.videojuegos = [juego for juego in self.videojuegos if juego.id != id]