from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Genere(models.Model):
    name = models.CharField(max_length=64, help_text='Indica el el género de la pélicula')

    def __str__(self):
        '''Devolvera la variable name en formato string'''
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=40, help_text='Titulo de la Pélicula')
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, help_text='Escriba una descripción de la pélicula')
    premiere = models.DateField()
    genere = models.ManyToManyField(Genere)

    def __str__(self):
        return self.title


class MovieInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='ID único para esta pélicula')
    '''Un UUID es unico '''
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)

    LOAD_CONST = (
        ('p', 'En cine'),
        ('d', 'DVD'),
        ('n', 'Netflix'),
        ('t', 'Todas'),
    )

    status = models.CharField(max_length=1, choices=LOAD_CONST,
                              blank=True, default='p', help_text='En que plataforma está disponible')

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_abdolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


