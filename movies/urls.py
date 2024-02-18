from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('movie/<slug:movie_slug>', ShowMovie.as_view(), name='show_movie'),
    path('series/', CatSeries.as_view(), name='series'),
    path('anime/', CatAnime.as_view(), name='anime'),
    path('mult/', CatMult.as_view(), name='mult'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),

]