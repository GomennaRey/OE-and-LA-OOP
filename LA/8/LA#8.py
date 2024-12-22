class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 

Libro = Book ("StarWars" , "Timothy Zahn")
del Libro.author
Librobro = Book ("GameofThrones" , "George R. Martin")
print(Librobro.author)
