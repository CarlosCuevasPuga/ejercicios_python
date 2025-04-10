from datetime import datetime

class Persona:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: datetime, casado: bool, divorciado: bool):
        self.nombre = nombre
        self.dni = dni
        
        if fecha_nacimiento <= datetime.now():
            self.fecha_nacimiento = fecha_nacimiento
        else: self.fecha_nacimiento = datetime.now()

        self.casado = casado
        self.divorciado = divorciado

        if self.casado and divorciado:
            self.casado == False
            self.divorciado == False

    def __str__(self) -> str:
        return (
            f"{self.nombre}\n"
            f"DNI: {self.dni}, fecha de nacimiento: {self.fecha_nacimiento}, estado civil: {self.estado_civil()}"
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, Persona):
            return self.dni == other.dni
        else:
            return False

    def estado_civil(self) -> str:
        if self.casado == True and self.divorciado == False:
            return "casado"
        elif self.divorciado == True and self.casado == False:
            return "divorciado"
        else:
            return "soltero"