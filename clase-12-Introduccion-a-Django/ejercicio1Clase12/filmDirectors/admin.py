import imp
from django.contrib import admin

# Register your models here.
from .models import Genere, Movie, Director, MovieInstance

admin.site.register(Genere)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(MovieInstance)