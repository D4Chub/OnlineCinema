from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster', 'time')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster', 'time')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class MultAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster', 'time')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster', 'time')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class ScreenWriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(ScreenWriter, ScreenWriterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Anime, AnimeAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Mult, MultAdmin)


