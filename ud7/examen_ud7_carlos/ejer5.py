from PlantillaEmpleados import PlantillaEmpleados
from Empleado import Empleado
from datetime import datetime

empleados = [
    Empleado("Laura Martínez", "12345678A", datetime(1987, 3, 12), False, False, 2800, datetime(2015, 6, 1), [datetime(2019, 2, 1), datetime(2020, 6, 1), datetime(2021, 9, 1), datetime(2022, 3, 1), datetime(2023, 11, 1), datetime(2021, 1, 1), datetime(2022, 7,1), datetime(2024, 12, 1)]),

    Empleado("Carlos Gómez", "87654321B", datetime(1990, 11, 8), True, False, 2500, datetime(2018, 9, 15), [datetime(2019, 5, 1), datetime(2020, 12, 1), datetime(2022, 7, 1), datetime(2023, 4, 1), datetime(2025, 1, 1), datetime(2020, 3, 1), datetime(2021, 8, 1), datetime(2023, 6, 1)]),
    
    Empleado("Ana Rodríguez", "11223344C", datetime(1985, 7, 23), False, True, 2700, datetime(2020, 1, 20),[]),
    
    Empleado("Miguel Torres", "44332211D", datetime(1993, 4, 5), False, False, 2400, datetime(2019, 4, 10), [datetime(2020, 1, 1), datetime(2021, 10, 1), datetime(2023, 8, 1), datetime(2024, 2, 1)]),
    
    Empleado("Beatríz Navarro", "99887766E", datetime(1988, 12, 30), True, False, 3000, datetime(2017, 11, 3), [datetime(2022, 9, 1)])
]

Plantilla = PlantillaEmpleados()

for empleado in empleados:
    Plantilla.meter_empleados(empleado)

print(Plantilla)

print("-" * 40)

dnis = ["12345678A", "87654321B", "11223344C", "44332211D"]

Plantilla.despedir(dnis)

print(Plantilla)