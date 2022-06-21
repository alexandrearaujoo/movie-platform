from rest_framework import serializers

from genres.serializers import GenreSerializer
from reviews.serializers import ReviewSerializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField(max_length=255)

    genres = GenreSerializer(many=True)

    reviews = ReviewSerializers(many=True)