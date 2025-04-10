from datetime import datetime

class Coche:
    def __init__(self, marca: str, modelo: str, año: int):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return (
            f"Marca: {self.marca}, "
            f"Modelo: {self.modelo}, "
            f"Año: {self.año}"
        )

    def actualizar_año(self, nuevo_año: int):
        self.año = nuevo_año

# Crear una instancia del coche
mi_coche = Coche("Toyota", "Corolla", 2020)

# Mostrar la información
print(mi_coche.mostrar_info())  # "Marca: Toyota, Modelo: Corolla, Año: 2020"

# Actualizar el año
mi_coche.actualizar_año(2023)
print(mi_coche.mostrar_info())  # "Marca: Toyota, Modelo: Corolla, Año: 2023"