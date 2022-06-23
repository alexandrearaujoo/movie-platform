from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework.authentication import TokenAuthentication
from .helpers import response_formatted


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
        reviews = Review.objects.filter(movie=movie_id)

        if not reviews:
            return Response({"message": "Review not found"}, status.HTTP_400_BAD_REQUEST)

        serializer = ReviewSerializer(reviews, many=True)

        serializer_data = []

        for values in serializer.data:
            serializer_data.append(response_formatted(values))

        return Response(serializer_data, status.HTTP_200_OK)

    def post(self, request, movie_id):

        serializer = ReviewSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)

        serializer.save(critic=request.user.id, movie=movie_id)

        serializer_data = response_formatted(serializer.data)

        return Response(serializer_data, status.HTTP_201_CREATED)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)

        review.delete()

        return Response({}, status.HTTP_204_NO_CONTENT)
        


