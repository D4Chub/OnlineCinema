from django.contrib import admin
from django.utils.html import format_html

from movies.models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('logo', 'id', 'title', 'poster', 'time')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    def logo(self, obj):
        if not obj.poster:
            return None
        if obj.poster.url:
            return format_html(f"""
            <div style="        
            height:150px;
            width:100px; 
            background-image:url({obj.poster.url});
            background-size:cover;        
            margin:auto;">        
            """)



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(ScreenWriter)
class ScreenWriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}




