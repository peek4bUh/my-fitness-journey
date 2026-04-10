from django.urls import path
from apps.exercises import views

urlpatterns = [
    # Exercises
    path("exercises", views.ExerciseList.as_view(), name="exercise-list"),
    path("exercises/<int:pk>", views.ExerciseDetail.as_view(),
         name="exercise-detail"),

    # Difficulties
    path("difficulties", views.ExerciseDifficultyList.as_view(),
         name="difficulty-list"),
    path("difficulties/<int:pk>",
         views.ExerciseDifficultyDetail.as_view(), name="difficulty-detail"),
]
