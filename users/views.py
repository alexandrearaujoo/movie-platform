from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from users.serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
