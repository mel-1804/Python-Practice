#  Nuevo ejercicio: Clase Library con múltiples libros
# Ahora vas a crear dos clases:

# 1. Book (igual que antes)
# 2. Library, que:
# Almacena una lista de libros

# Tiene los siguientes métodos:
# add_book(book) ➡️ agrega un objeto Book a la lista.
# list_books() ➡️ imprime los resúmenes de todos los libros en la biblioteca.
# find_books_by_author(author_name) ➡️ devuelve todos los libros de ese autor.

# 💡 Tips:
# Usa una lista (self.books) dentro de Library para almacenar los objetos Book.
# Usa isinstance(book, Book) para asegurarte de que estás agregando un libro válido (opcional).

class Book:
    def __init__(self, title, author, year):
        # aquí asignas los atributos
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        # aquí retornas el string con el resumen
        return f"{self.title} by {self.author}, published in {self.year}."


class Library:
    def __init__(self):
        self.books = []  # inicializas una lista vacía para almacenar libros

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: El objeto no es una instancia de la clase Book.")


    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book.get_summary())


    def find_books_by_author(self, author_name):
        return [book for book in self.books if book.author == author_name]

# Creamos algunos libros
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Animal Farm", "George Orwell", 1945)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 1937)

# Creamos la biblioteca
library = Library()

# Agregamos libros
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Listamos todos los libros
print("Todos los libros:")
library.list_books()

# Buscamos libros por autor
print("\nLibros de George Orwell:")
orwell_books = library.find_books_by_author("George Orwell")
for book in orwell_books:
    print(book.get_summary())
