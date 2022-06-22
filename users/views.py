from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.models import User

from users.serializers import LoginSerializer, UserSerializer


class UserView(APIView):

    def get(self, request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class UserViewDetail(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)

        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request): 
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(username=email, password=password)

        if user: 
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status.HTTP_200_OK)

        return Response(
            {"detail": "invalid email or password"},
            status.HTTP_401_UNAUTHORIZED
        )
