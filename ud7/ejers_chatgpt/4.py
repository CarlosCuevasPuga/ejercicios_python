class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __str__(self) -> str:
        return f"Titulo: {self.titulo}, Autor: {self.autor}."

mi_libro = Libro("1984", "George Orwell")
print(mi_libro)  # "Título: 1984, Autor: George Orwell"