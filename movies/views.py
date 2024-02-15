from django.shortcuts import render

from movies.models import *


def home(request):
    movies = Movie.objects.all()
    genre = Genre.objects.all()
    return render(request, 'movies/home.html', {'movies': movies, 'genre': genre})
