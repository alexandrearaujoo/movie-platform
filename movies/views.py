from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from models import Movie
from serializers import MovieSerializer

class MovieView(APIView):
    def get(self, request): 
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class MovieViewDetail(APIView):
    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)
