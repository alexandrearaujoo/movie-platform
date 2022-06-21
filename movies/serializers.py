from rest_framework import serializers
from genres.models import Genre

from genres.serializers import GenreSerializer
from movies.models import Movie
from reviews.serializers import ReviewSerializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField(max_length=255)

    genres = GenreSerializer(many=True)


    def create(self, validated_data):
        genres = validated_data.pop('genres')

        movie = Movie.objects.create(**validated_data)

        for genre in genres:
            g , _ = Genre.objects.get_or_create(**genre)
            movie.genres.add(g)

        return movie