from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from movies.models import *


def home(request):
    movies = Movie.objects.all()
    genre = Genre.objects.all()
    return render(request, 'movies/home.html', {'movies': movies, 'genre': genre})


class ShowMovie(View):
    template_name = 'movies/movie_info.html'

    def get(self, request, movie_slug):
        movie_info = Movie.objects.get(slug=movie_slug)
        movie = get_object_or_404(Movie, slug=movie_slug)
        genre = Genre.objects.all()
        actor = Actor.objects.all()
        director = Director.objects.all()
        screenwriter = Director.objects.all()

        context = {
            'movie': movie,
            'movie_info': [movie_info],
            'genre': genre,
            'actor': actor,
            'director': director,
            'screenwriter': screenwriter,
        }
        return render(request, self.template_name, context=context)


class Login(View):
    template_name = 'movies/login.html'

    def get(self, request):
        return render(request, self.template_name)
