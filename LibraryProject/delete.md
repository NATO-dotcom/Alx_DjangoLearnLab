book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

# Confirm deletion
remaining_books = Book.objects.all()
print(remaining_books)
# Expected Output: <QuerySet []>