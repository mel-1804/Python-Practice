# 🚀 Ejercicio: Clase Book (Libro)
# Crea una clase Book que represente un libro con las siguientes propiedades:

# title (título)

# author (autor)

# year (año de publicación)

# Y un método que:

# get_summary() que devuelva un string con el resumen del libro, como:

# "Harry Potter" by J.K. Rowling, published in 1997.

# 💻 Plantilla para empezar:
# class Book:
#     def __init__(self, title, author, year):
#         # aquí asignas los atributos

#     def get_summary(self):
#         # aquí retornas el string con el resumen

# Y luego puedes crear una instancia así:
# my_book = Book("Harry Potter", "J.K. Rowling", 1997)
# print(my_book.get_summary())

class Book:
    def __init__(self, title, author, year):
        # aquí asignas los atributos
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        # aquí retornas el string con el resumen
        return f"{self.title} by {self.author}, published in {self.year}."

my_book = Book("Harry Potter", "J.K. Rowling", 1997)
print(my_book.get_summary())
