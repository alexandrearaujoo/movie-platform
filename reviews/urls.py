from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/reviews/', views.ReviewViewDetail.as_view()),
    path('reviews/', views.ReviewView.as_view()),
    path('reviews/<int:review_id>', views.ReviewViewDetail.as_view())
]