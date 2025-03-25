from datos import get_usuarios
from datos import get_juegos
from Videojuego import Videojuego

def videojuegos_segun_edad(nombre: str) -> list:
    for usuario in get_usuarios():
        if usuario.nombre == nombre and usuario.edad() >= 18:
            return [juegos for juegos in get_juegos()]
        elif usuario.nombre == nombre and usuario.edad() < 18:
            edad_usuario = usuario.edad()
            return [juegos for juegos in get_juegos() if juegos.PEGI < edad_usuario]

def saldo_usuario(nombre) -> float:
    for usuario in get_usuarios():
        if usuario.nombre == nombre:
            return usuario.saldo

def convertir_a_entero(string: str) -> int:
    entero = int(string)
    return entero