from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from movies.models import Movie

from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewView(APIView):
    def get(self, request):
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

class ReviewViewDetail(APIView):
    def get(self, request, movie_id):
        reviews = get_object_or_404(Review, movie_id=movie_id)

        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)

        serializer = ReviewSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)

        serializer.data.movie_id = movie.id

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
        


