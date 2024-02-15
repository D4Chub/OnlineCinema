from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class ScreenWriter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сценарист'
        verbose_name_plural = 'Сценаристы'


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Movie(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    poster = models.ImageField(verbose_name='Постер', upload_to='posters/')
    description = models.TextField(verbose_name='Описание')
    year = models.IntegerField(verbose_name='Год производства')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    actor = models.ManyToManyField(Actor, verbose_name='В главных ролях')
    directors = models.ManyToManyField(Director, verbose_name='Режиссер')
    screenwriter = models.ManyToManyField(ScreenWriter, verbose_name='Сценарист')
    premiere = models.DateField(verbose_name='Премьера')
    time = models.CharField(verbose_name='Время', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'





