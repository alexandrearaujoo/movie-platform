from rest_framework import serializers
from reviews.models import Review

from users.serializers import UserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    critic = UserSerializer()

    class Meta:
        model = Review
        fields = ['id','stars', 'review', 'spoilers', 'recomendations']
        read_only_fields = ['id', 'movie_id', 'critic']