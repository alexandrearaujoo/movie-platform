from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/reviews/', views.ReviewViewDetail.as_view()),
    path('movies/reviews/', views.ReviewViewDetail.as_view())
]