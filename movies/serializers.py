from rest_framework import serializers
from .models import * 


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    actor = serializers.StringRelatedField(many=True)
    directors = serializers.StringRelatedField(many=True)
    screenwriter = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ('title', 'poster', 'description', 'category', 'year', 'genre', 'actor', 'directors', 'screenwriter', 'premiere', 'time')


