from django.contrib import admin
from genres.models import Genre
from movies.models import Movie
from reviews.models import Review

from users.models import User

admin.site.register(User)
admin.site.register(Review)
admin.site.register(Movie)
admin.site.register(Genre)
