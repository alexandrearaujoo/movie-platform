from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework.authentication import TokenAuthentication

from movies.permissions import MoviePermissionsCustom
from .models import Movie
from .serializers import MovieSerializer

class MovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermissionsCustom]

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermissionsCustom]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, movie_id): 
        movie = get_object_or_404(Movie, pk=movie_id)

        serializer = MovieSerializer(movie, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)

        movie.delete()

        return Response({},status.HTTP_204_NO_CONTENT)
