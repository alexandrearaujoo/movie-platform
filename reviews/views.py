from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework.authentication import TokenAuthentication
from .permissions import ReviewPermissionsCustom
from project.pagination import CustomPageNumberPagination
from .helpers import response_formatted

from .models import Review
from .serializers import ReviewSerializer

class ReviewView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewPermissionsCustom]

    def get(self, request):
        reviews = Review.objects.all()

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        serializer_data = []

        for values in serializer.data:
            serializer_data.append(response_formatted(values))

        return self.get_paginated_response(serializer_data)

class ReviewViewDetail(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewPermissionsCustom]
    
    def get(self, request, movie_id):
        reviews = Review.objects.filter(movie=movie_id)

        if not reviews:
            return Response({"message": "Movie review not found"}, status.HTTP_400_BAD_REQUEST)

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        serializer_data = []

        for values in serializer.data:
            serializer_data.append(response_formatted(values))

        return self.get_paginated_response(serializer_data)

    def post(self, request, movie_id):

        serializer = ReviewSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)

        serializer.save(critic=request.user.id, movie=movie_id)

        serializer_data = response_formatted(serializer.data)

        return Response(serializer_data, status.HTTP_201_CREATED)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)

        self.check_object_permissions(request, review)

        review.delete()

        return Response({}, status.HTTP_204_NO_CONTENT)
        


