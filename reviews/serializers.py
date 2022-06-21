from rest_framework import serializers

from users.serializers import UserSerializer

class ReviewSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    starts = serializers.IntegerField() 
    review = serializers.CharField(max_length=255)
    spoilers = serializers.BooleanField(default=False)
    recomendation = serializers.CharField(max_length=50)

    user = UserSerializer()