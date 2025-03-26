class ModeloCoche:

    def __init__(self, marca: str, modelo: str, año_fabricacion: int, peso: int, tipo_motor: str, potencia: int, automatico: bool, num_puertas: int, num_asientos: int, consumo: float, deposito: float):
        self.marca = marca
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion
        self.peso = peso
        self.tipo_motor = tipo_motor
        self.potencia = potencia
        self.automatico = automatico
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.consumo = consumo
        self.deposito = deposito

    def __str__(self) -> str:
        return(
            f"Marca: {self.marca},"
            f"Modelo: {self.modelo},"
            f"año de fabricación: {self.año_fabricacion},"
            f"Peso: {self.peso},"
            f"Tipo de motor: {self.tipo_motor},"
            f"Potencia: {self.potencia},"
            f"Automático: {self.automatico},"
            f"Número de puertas: {self.num_puertas},"
            f"Número de asientos: {self.num_asientos},"
            f"Consumo: {self.consumo} litro/s,"
            f"Depósito: {self.deposito} litro/s"
        )

    def __eq__(self, other) -> bool:
        if isinstance(other, ModeloCoche):
            return self.modelo == other.modelo
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, ModeloCoche):
            return self.potencia < other.potencia

    def __gt__(self, other) -> bool:
        if isinstance(other, ModeloCoche):
            return self.potencia > other.potencia

    def autonomia(self) -> float:
        return round((self.deposito / self.consumo) * 100, 2)