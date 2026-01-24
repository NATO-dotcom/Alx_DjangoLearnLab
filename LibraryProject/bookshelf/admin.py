from django.contrib import admin
from .models import Book

# Customizing the admin interface
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add a search bar to filter by title or author
    search_fields = ('title', 'author')
    
    # Add a filter sidebar for publication year
    list_filter = ('publication_year',)

# Register the model with its custom admin class
admin.site.register(Book, BookAdmin)
