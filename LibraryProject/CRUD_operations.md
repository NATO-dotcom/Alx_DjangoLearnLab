# Django ORM CRUD Operations

## 1. Create
# Command:
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Output:
# <Book: 1984>

## 2. Retrieve
# Command:
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

# Output:
# 1984 George Orwell 1949

## 3. Update
# Command:
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.title)

# Output:
# Nineteen Eighty-Four

## 4. Delete
# Command:
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
print(Book.objects.all())

# Output:
# <QuerySet []>