from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('movie/<slug:movie_slug>', ShowMovie.as_view(), name='show_movie'),
    path('category/<slug:cat_slug>', ShowCategory.as_view(), name='category'),
    path('about/', About.as_view(), name='about'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('search/', Search.as_view(), name='search'),

]