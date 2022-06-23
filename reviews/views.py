from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.authentication import TokenAuthentication
from users.models import User
from users.serializers import UserSerializer 

from .models import Review
from .serializers import ReviewSerializer

class ReviewView(APIView):
    def get(self, request):
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

class ReviewViewDetail(APIView):
    authentication_classes = [TokenAuthentication]
    
    def get(self, request, movie_id):
        reviews = get_object_or_404(Review, movie_id=movie_id)

        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, movie_id):

        serializer = ReviewSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user.id, movie=movie_id)

        return Response(serializer.data, status.HTTP_201_CREATED)
        


