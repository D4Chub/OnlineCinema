from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('movie/<slug:movie_slug>', ShowMovie.as_view(), name='show_movie')
]