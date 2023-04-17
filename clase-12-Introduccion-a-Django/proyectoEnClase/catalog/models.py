from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
'''al crear un modelo se debe heredar de "models.Model"'''
class Genere(models.Model):
    name = models.CharField(
        max_length=64, help_text='Pon el nombre del genero')

    def __str__(self):
        '''una reprentacion informal de un objeto. Devolviendo la variable 'name' en formato string para utilizarla despues'''
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=100, help_text='Pon aquí de que va el libro')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='El ISBN es de 13 caracteres')
    genere = models.ManyToManyField(Genere)

    def __str__(self):
        return self.title

    def get_abasolute_url(self):
        return reverse('book-detail', args =[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID único para este libro')
    '''Un UUID es unico '''
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAD_CONST = (
        ('m', 'Mantenimiento'),
        ('o', 'On loan'),
        ('a', 'Avalibre'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAD_CONST, blank=True, default='m', help_text='Disponibilidad del Libro')

    class Meta():
        ordering = ['due_back']

    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_abdolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name,self.first_name)