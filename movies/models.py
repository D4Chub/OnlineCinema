from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Person(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Genre(Person):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Director(Person):

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

    def __str__(self):
        return self.name


class ScreenWriter(Person):

    class Meta:
        verbose_name = 'Сценарист'
        verbose_name_plural = 'Сценаристы'

    def __str__(self):
        return self.name


class Actor(Person):

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

    def __str__(self):
        return self.name


class Category(Person):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

class Movie(models.Model):

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'

    title = models.CharField(verbose_name='Название', max_length=100,null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    poster = models.ImageField(verbose_name='Постер', upload_to='posters',null=True, blank=True)
    description = models.TextField(verbose_name='Описание',null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)
    year = models.CharField(max_length=50, verbose_name='Год производства',null=True, blank=True)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр', null=True, blank=True)
    trailer = models.URLField(verbose_name='Ссылка на трейлер', null=True, blank=True)
    actor = models.ManyToManyField(Actor, verbose_name='В главных ролях', null=True, blank=True)
    directors = models.ManyToManyField(Director, verbose_name='Режиссер',null=True, blank=True)
    screenwriter = models.ManyToManyField(ScreenWriter, verbose_name='Сценарист',null=True, blank=True)
    premiere = models.DateField(verbose_name='Премьера',null=True, blank=True)
    time = models.CharField(verbose_name='Время', max_length=30,null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)

    def get_absolute_url(self):
        return reverse('show_movie', kwargs={'movie_slug': self.slug})

    def __str__(self):
        return self.title
