from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('movie/<slug:movie_slug>', ShowMovie.as_view(), name='show_movie'),
    path('series/<slug:series_slug>', ShowSeries.as_view(), name='show_series'),
    path('series/<slug:anime_slug>', ShowAnime.as_view(), name='show_anime'),
    path('series/<slug:mult_slug>', ShowMult.as_view(), name='show_mult'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),

]