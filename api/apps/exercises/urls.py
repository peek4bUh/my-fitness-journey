from django.urls import path

from apps.exercises import views


urlpatterns = [
    path("exercises", views.ExerciseList.as_view()),
    path("exercises/<int:pk>", views.ExerciseDetail.as_view()),
]
