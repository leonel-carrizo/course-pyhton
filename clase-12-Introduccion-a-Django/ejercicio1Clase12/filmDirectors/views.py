from django.shortcuts import render
from . models import Movie, Director, MovieInstance, Genere
# Create your views here.

def index(request):
    num_movies = Movie.objects.all().count()
    num_instances = MovieInstance.objects.all().count()
    num_directors = Director.objects.all().count()

    plataformas = MovieInstance.objects.filter(status__exact='p').count()

    return render(
        request,
        'index.html',
        context={
            'num_movies': num_movies,
            'num_directors': num_directors,
            'num_instances': num_instances,
            'plataformas': plataformas,
        }
    )