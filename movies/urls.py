from django.urls import path

from movies import views

urlpatterns = [
    path('movies/', views.APIView.as_view()),
    path('movies/<int:movie_id>', views.MovieViewDetail.as_view())
]