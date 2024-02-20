from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class ScreenWriter(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сценарист'
        verbose_name_plural = 'Сценаристы'


class Actor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Movie(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    poster = models.ImageField(verbose_name='Постер', upload_to='posters')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)
    year = models.CharField(max_length=50, verbose_name='Год производства')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    actor = models.ManyToManyField(Actor, verbose_name='В главных ролях')
    directors = models.ManyToManyField(Director, verbose_name='Режиссер')
    screenwriter = models.ManyToManyField(ScreenWriter, verbose_name='Сценарист')
    premiere = models.DateField(verbose_name='Премьера')
    time = models.CharField(verbose_name='Время', max_length=30)

    def get_absolute_url(self):
        return reverse('show_movie', kwargs={'movie_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'


