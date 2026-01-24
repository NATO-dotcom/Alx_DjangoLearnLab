from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    # Using the filter method to find books belonging to the author
    return Book.objects.filter(author=author)

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    # Accessing the many-to-many relationship
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    # Accessing the one-to-one relationship via the related object
    return Librarian.objects.get(library=library)