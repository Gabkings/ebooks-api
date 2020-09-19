from django.contrib import admin

# Register your models here.
from books.models import BooksModel, BookReviews

admin.site.register(BookReviews)
admin.site.register(BooksModel)