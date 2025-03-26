from ModeloCoche import ModeloCoche
from datetime import datetime

class Coche(ModeloCoche):
    def __init__(self, n_bastidor: str, matricula: str, fecha_matricula: datetime, color: str, fecha_proxima_itv: datetime, fecha_itv_actual: datetime, precio_base: float, precio_venta: float):
        self.n_bastidor = n_bastidor
        self.matricula = matricula
        self.fecha_matricula = fecha_matricula
        self.color = color

        if fecha_proxima_itv > datetime.now().year:
            self.fecha_proxima_itv = self.fecha_proxima_itv
        else:
            self.fecha_proxima_itv = datetime.now().year
        
        self.fecha_itv_actual = fecha_itv_actual
        
        if self.precio_base >= 0:
            self.precio_base = round(precio_base, 2)
        else:
            self.precio_base = 0

        self.precio_venta = round(precio_venta, 2)

    def actualizar_itv(dia_pasada: str):
        pass

    def aplicar_descuento(descuento: float):
        pass

    def __eq__(self, other) -> bool:
        if isinstance(other, Coche):
            return self.matricula == other.matricula
        return False