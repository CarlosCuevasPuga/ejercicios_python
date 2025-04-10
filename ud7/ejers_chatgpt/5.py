class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, tipo: str):
        super().__init__(marca, modelo)

        self.tipo = tipo

    def mostrar_tipo(self) -> str:
        return f"Tipo: {self.tipo}"

class CocheDeCarreras(Vehiculo):
    def __init__(self, marca: str, modelo: str, velocidad_maxima: int):
        super().__init__(marca, modelo)

        self.velocidad_maxima = velocidad_maxima

    def mostrar_velocidad_maxima(self) -> str:
        return f"Velocidad Maxima: {self.velocidad_maxima}"


# Crear una instancia de la clase Bicicleta
mi_bici = Bicicleta("Trek", "X-Caliber", "montaña")
print(mi_bici.mostrar_tipo())  # "Tipo: montaña"

# Crear una instancia de la clase CocheDeCarreras
mi_coche = CocheDeCarreras("Ferrari", "488 GTB", 340)
print(mi_coche.mostrar_velocidad_maxima())  # "Velocidad Maxima: 340"