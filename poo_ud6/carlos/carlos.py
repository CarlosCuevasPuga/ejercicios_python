from Libro import Libro

# EJER9

mejores_libros_mundiales = [
    Libro("Crimen y castigo", "Fiódor Dostoievski", 671, ["Novela", "Filosofia", "Psicologia"], 10),
    Libro("Guerra y paz", "León Tolstói", 1225, ["Novela", "Historica"], 10),
    Libro("Anna Karénina", "León Tolstói", 864, ["Novela", "Drama", "Romance"], 9),
    Libro("El maestro y Margarita", "Mijaíl Bulgákov", 384, ["Fantasia", "Satirica"], 9),
    Libro("Los hermanos Karamázov", "Fiódor Dostoievski", 1013, ["Novela", "Filosofia", "Drama"], 10),
    Libro("1984", "George Orwell", 328, ["Distopía", "Ciencia", "Ficción"], 10),
    Libro("Cien años de soledad", "Gabriel García Márquez", 471, ["Realismo mágico", "Drama"], 10),
    Libro("Ulises", "James Joyce", 730, ["Experimental", "Filosofia"], 8),
    Libro("Moby-Dick", "Herman Melville", 635, ["Aventura", "Clasico"], 9),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863, ["Aventura", "Clasico", "Sátira"], 10)
]

# EJER10

# Encontrar los libros escritos por Dostoievski con más de 1000 páginas
libros_dost_1000pg = [libro.nombre for libro in mejores_libros_mundiales if libro.paginas >= 1000 and libro.autores == "Fiódor Dostoievski"]
print(f"Los libros escritos por Dostoievski con mas de 1000 páginas son:\n")
for libro in libros_dost_1000pg:
    print(libro)

print("\n----------------\n")

# Encontrar los libros con menos de 400 páginas
libros_menor_400pg = [libro.nombre for libro in mejores_libros_mundiales if libro.paginas < 400]
print("los libros con menos de 400 páginas son:\n")
for libro in libros_menor_400pg:
    print(libro)

print("\n----------------\n")

# Encontrar los libros cuyo nombre es un número
nombres_libros = [libro.nombre for libro in mejores_libros_mundiales]
libro_nombre_nums = [libro for libro in nombres_libros if "0" in libro or "1" in libro or "2" in libro or "3" in libro or "4" in libro or "5" in libro or "6" in libro or "7" in libro or "8" in libro or "9" in libro]
print("los libros cuyo nombre es un número son:\n")
for libro in libro_nombre_nums:
    print(libro)

print("\n----------------\n")

# Encontrar (sin repetir) los escritores de la lista
nombres_autores = [libro.autores for libro in mejores_libros_mundiales]
nombres_autores_sin_repetir = []
for nombre in nombres_autores:
    if not nombre in nombres_autores_sin_repetir:
        nombres_autores_sin_repetir.append(nombre)
print("Los escritores de los libros son:\n")
for nombre in nombres_autores_sin_repetir:
    print(nombre)

#EJER11

mejores_libros_españoles = [
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863, ["Aventura", "Clasico", "Sátira"], 10),
    Libro("La Regenta", "Leopoldo Alas Clarín", 928, ["Novela","Realismo","Drama"], 9),
    Libro("Fortunata y Jacinta", "Benito Pérez Galdós", 1056, ["Novela","Costumbrismo","Drama"], 9),
    Libro("Campos de Castilla", "Antonio Machado", 208, ["Poesía","Reflexion"], 9),
    Libro("Platero y yo", "Juan Rámon Jiménez", 138, ["Narrativa","Poesia en prosa"], 8),
    Libro("Bodas de sangre", "Federico García Lorca", 128, ["Teatro","Tragedia","Poesía"], 9),
    Libro("La colmena", "Camilo José Cela", 304, ["Novela","Costumbrismo"], 8),
    Libro("Nada", "Carmen Laforet", 288, ["Novela","Existencialismo"], 9),
    Libro("El camino", "Miguel Delibes", 176, ["Novela","Realismo"], 8),
    Libro("Los santos inocentes", "Miguel Delibes", 254, ["Novela","Drama","Social"], 9)
]

# Encontrar los mejores libros de la historia que además son españoles
libros_españoles_en_mundiales = []
for libro_mundial in mejores_libros_mundiales:
    for libro_español in mejores_libros_españoles:
        if libro_mundial.nombre == libro_español.nombre:
            libros_españoles_en_mundiales.append(libro_español.nombre)

print("los mejores libros de la historia que además son españoles son:\n")
print(libros_españoles_en_mundiales)

print("\n----------------\n")

# Encontrar los mejores escritores españoles cuyos libros NO estén dentro de los mejores libros escritos por la humanidad
mejores_escritores_españoles = []
for libro_mundial in mejores_libros_mundiales:
    for libro_español in mejores_libros_españoles:
        if libro_mundial.autores != libro_español.autores and not libro_español.autores in mejores_escritores_españoles:
            mejores_escritores_españoles.append(libro_español.autores)

print("Los mejores escritores españoles cuyos libros NO estén dentro de los mejores libros escritos por la humanidad son:\n")
for escritor in mejores_escritores_españoles:
    print(escritor)

print("\n---------------\n")

# Encontrar los mejores libros (españoles o mundiales) que empiezan por D (no puede haber repeticiones)
nombre_libros_mundiales = [libro.nombre for libro in mejores_libros_mundiales]
nombre_libros_españoles = [libro.nombre for libro in mejores_libros_españoles]
mejores_libros_españoles_mundiales = []

for libro_español in nombre_libros_españoles:
    if libro_español[0] == "D":
        mejores_libros_españoles_mundiales.append(libro_español)
for libro_mundial in nombre_libros_mundiales:
    if libro_mundial[0] == "D" and not libro_mundial in mejores_libros_españoles_mundiales:
        mejores_libros_españoles_mundiales.append(libro_mundial)

print("los mejores libros (españoles o mundiales) que empiezan por D son:\n")
print(mejores_libros_españoles_mundiales)

print("\n---------------\n")

# ¿Quién es el mejor escritor español? (Calcular el mejor escritor español como aquel que más títulos tiene en la lista de mejores libros españoles)
i = 0
autor_con_mas_libros = ""
nombre_autores_españoles = [libro.autores for libro in mejores_libros_españoles]
for autor in nombre_autores_españoles:
    if nombre_autores_españoles.count(autor) > i:
        autor_con_mas_libros = autor

print("El mejor autor español es:\n")
print(autor_con_mas_libros)