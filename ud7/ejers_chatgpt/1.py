class persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> str:
        return f"Hola mi nombre es {self.nombre} y tengo {self.edad} años"

    

# Crear una instancia de la clase Persona
persona1 = persona("Juan", 25)

# Llamar al método saludar
print(persona1.saludar())