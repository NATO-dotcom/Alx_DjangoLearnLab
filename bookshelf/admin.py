from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in admin list view
    search_fields = ('title', 'author')                    # Add search bar for these fields
    list_filter = ('publication_year',)                    # Add filters for publication year
