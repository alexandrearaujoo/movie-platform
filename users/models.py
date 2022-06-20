from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()