class animal:

    def hablar(self) -> str:
        return "Hace un sonido"

class Perro(animal):

    def hablar(self) -> str:
        return "Guau"

# Crear una instancia de la clase Perro
mi_perro = Perro()

# Llamar al método hablar()
print(mi_perro.hablar())  # Salida: "Guau"