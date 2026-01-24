book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

# Verify change
print(Book.objects.get(author="George Orwell").title)
# Expected Output: Nineteen Eighty-Four