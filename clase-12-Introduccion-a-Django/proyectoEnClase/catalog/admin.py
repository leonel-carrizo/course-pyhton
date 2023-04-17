from django.contrib import admin

# Register your models here.
from .models import Author, Genere, Book, BookInstance

admin.site.register(Author)
admin.site.register(Genere)
admin.site.register(Book)
admin.site.register(BookInstance)
