from dataclasses import dataclass

@dataclass
class Pelicula:
    nombre: str
    duracion: int
    actores: list

Peliculas = [
    Pelicula("El Padrino", 175, ["Mario Brando", "Al Pacino", "James Caan"]),
    Pelicula("Interestelar", 169, ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"]),
    Pelicula("El Caballero Oscuro", 152, ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),
    Pelicula("Forrest Gump", 142, ["Tom Hanks", "Robin Wright", "Gary Sinise"]),
    Pelicula("Náufrago", 143, ["Tom Hanks", "Helen Hunt", "Nick Searcy"])
]

for pelicula in Peliculas:
    print(pelicula)

print("-" * 120)

peliculas_actores_con_h = [pelicula for pelicula in Peliculas if "H" in pelicula.actores and pelicula.duracion > 150]

for pelicula in peliculas_actores_con_h:
    print(pelicula)