from django.views.generic import ListView
from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from django.views import View

from movies.models import *


class Home(View):
    template_name = 'movies/index.html'

    def get(self, request):
        movies = Movie.objects.all()
        genre = Genre.objects.all()
        cat = Category.objects.all()

        context = {
            'movies': movies,
            'genre': genre,
            'cat': cat
        }
        return render(request, self.template_name, context)


class ShowMovie(View):
    template_name = 'movies/movie-info.html'

    def get(self, request, movie_slug):
        movie_info = Movie.objects.get(slug=movie_slug)
        movie = get_object_or_404(Movie, slug=movie_slug)
        genre = Genre.objects.all()
        actor = Actor.objects.all()
        director = Director.objects.all()
        screenwriter = Director.objects.all()
        cat = Category.objects.all()
        context = {
            'movie': movie,
            'movie_info': [movie_info],
            'genre': genre,
            'actor': actor,
            'director': director,
            'screenwriter': screenwriter,
            'cat': cat

        }
        return render(request, self.template_name, context=context)


class ShowCategory(View):
    template_name = 'movies/index.html'

    def get(self, request, cat_slug):
        category = Category.objects.get(slug=cat_slug)
        movies = Movie.objects.filter(category=category)
        cat = Category.objects.all()
        context = {
            'movies': movies,
            'cat': cat,

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


class Search(ListView):
    model = Movie
    template_name = 'movies/movie_info.html'
    context_object_name = 'movie_info'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Movie.objects.filter(title__icontains=query)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        context['cat'] = Category.objects.all()
        return context