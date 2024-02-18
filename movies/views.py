from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from movies.models import *


class Home(View):
    template_name = 'movies/home.html'

    def get(self, request):
        movies = Movie.objects.all()
        genre = Genre.objects.all()
        context = {
            'movies': movies,
            'genre': genre,
        }
        return render(request, self.template_name, context)


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


class CatSeries(View):
    template_name = 'movies/series.html'

    def get(self, request):
        series = get_object_or_404(Series)
        genre = Genre.objects.all()
        context = {
            'series': [series],
            'genre': genre,
        }
        return render(request, self.template_name, context)


class CatAnime(View):
    template_name = 'movies/anime.html'

    def get(self, request):
        anime = Anime.objects.all()
        genre = Genre.objects.all()
        context = {
            'anime': anime,
            'genre': genre,
        }
        return render(request, self.template_name, context)


class CatMult(View):
    template_name = 'movies/mult.html'

    def get(self, request):
        mult = get_object_or_404(Mult)
        genre = Genre.objects.all()
        context = {
            'mult': [mult],
            'genre': genre,
        }
        return render(request, self.template_name, context)


class Login(View):
    template_name = 'movies/login.html'

    def get(self, request):
        return render(request, self.template_name)


class Register(View):
    template_name = 'movies/register.html'

    def get(self, request):
        return render(request, self.template_name)
