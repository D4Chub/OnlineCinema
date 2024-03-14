import os
import requests
from movies.models import *
from transliterate import slugify
from PIL import Image
from django.core.files.base import ContentFile 
from django.core.files.storage import default_storage


class STATUS:
    HTTP_OK = 200
    HTTP_CRATED = 201
    HTTP_BAD_REQUEST = 400
    HTTP_ACCESS_ERROR = 403
    ...


class RequestType:
    MOVIE = 'movie/'
    ...


class KinoSearchAPI:
  

    BASE_URL = 'https://api.kinopoisk.dev/v1.4/'

    def __init__(self, api_key: str):
        self.api_key = api_key

        if not self.api_key:
            raise ValueError("Value error API_KEY")

    @property
    def _headers(self) -> dict:
        """Generation headers for requests"""

        return {
            'X-API-KEY': self.api_key
        }

    def _get_request(self, request_type: str, additional_information: str = ''):
        """Request for getting movie from kinopoisk"""

        if not request_type:
            raise ValueError("None request_type")

        return requests.get(
            url=self.BASE_URL + request_type + additional_information, headers=self._headers
        )

    def get_movie_by_id(self, movie_id: str):
        """Send request for getting movie"""
        __response = self._get_request(request_type=RequestType.MOVIE,
                                       additional_information=movie_id)
        if __response.status_code == STATUS.HTTP_OK:
            return __response.json()
        else:
            raise ValueError("Request error")

kinopoisk_action = KinoSearchAPI(api_key=os.getenv('KINOPOISK_API_KEY'))


# Parsing kinopoisk data



def process_persons(persons: list[dict], profession: str, model_field: str, model_class: models.Model, movie: Movie) -> None:
    """Process persons information and add to the corresponding model."""
    person_list = [person for person in persons if person['enProfession'] == profession][:3]
    for person in person_list:
        person_obj, created = model_class.objects.get_or_create(name=person['name'])
        if not created:
            print(person['name'])
        field = getattr(movie, model_field, None)
        
        if field is not None and isinstance(field, models.Manager):
            field.add(person_obj)
            movie.save()


def process_genres(genres: list[dict], movie: Movie) -> None:
    """Process genres information and add to the movie model."""
    for genre in genres:
        genre_obj, created = Genre.objects.get_or_create(name=genre['name'])
        if not created:
            print(genre['name'])
        movie.genre.add(genre_obj)
        movie.save()


def process_other_fields(field_data: str, model_field: str, movie: Movie, poster_title=None) -> None:
    """Process other fields information and add to the corresponding model."""
    if model_field == 'poster':
        # Download image from URL
        response = requests.get(field_data, stream=True).raw
        img = Image.open(response)
        
        # Getting bytes of an image
        img_bytes = img.tobytes() 

        # Saving image in 'media/posters'
        file_path = f'posters/{poster_title}.jpg'
        file_content = ContentFile(img_bytes)
        img.save(file_content, format='JPEG')
        default_storage.save(file_path, file_content)
        
        # Added image in Movie field 'poster'
        setattr(movie, model_field, file_path)
        movie.save()
    else:
        setattr(movie, model_field, field_data)
        movie.save()
        print(field_data)  


def get_kinopoisk_data() -> None:
    """Get all movie information and make processing."""
    movie_id_list = ['1253157']
    for movie_id in movie_id_list:
        substring = 'Length'
        
        movie_information: dict = kinopoisk_action.get_movie_by_id(movie_id=movie_id)
        persons: list = movie_information.get('persons', {})
        genres: list = movie_information.get('genres', {})[:4]
        title: str = movie_information.get('name', {})
        description: str = movie_information.get('description', {})
        year: int = movie_information.get('year', {})
        poster: str = movie_information.get('poster', {}).get('url')
        
        # Getting the names of all keys
        time_keys = list(movie_information.keys())
        
        # Getting the names of all keys with the substring 'Length'
        match_keys = [key for key in time_keys if substring in key]
        
        # Checking all keys, the key that is not empty is assigned
        for key in match_keys:
            value = movie_information.get(key)
            if value is not None and value != '':
                time = f'{value} мин.'
                
        
        premiere: str = movie_information.get('premiere', {}).get('world')[:10] 
        slug: str = slugify(title)
        
        movie: Movie = Movie.objects.create(title=title)
        
        # "Other" fields
        process_other_fields(title, 'title', movie)
        process_other_fields(description, 'description', movie)
        process_other_fields(poster, 'poster', movie, slug)
        process_other_fields(year, 'year', movie)
        process_other_fields(time, 'time', movie)
        process_other_fields(premiere, 'premiere', movie)
        process_other_fields(slug, 'slug', movie)
        

        # Related fields
        process_persons(persons, 'director', 'directors', Director, movie)
        process_persons(persons, 'writer', 'screenwriter', ScreenWriter, movie)
        process_persons(persons, 'actor', 'actor', Actor, movie)
        process_genres(genres, movie)




