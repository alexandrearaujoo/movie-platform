from django.db import models

from genres.models import Genre

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10)
    premiere = models.DateField()
    classification = models.IntegerField()
    synopsis = models.TextField()

    genres = models.ManyToManyField(
        'genres.Genre',
        related_name='genres'
    )


    def create(self, validated_data):
        genres = validated_data.pop('genres')

        genres, _ = Genre.objects.get_or_create(**genres)
        movie = Movie.objects.create(**validated_data, genres=genres)

        return movie