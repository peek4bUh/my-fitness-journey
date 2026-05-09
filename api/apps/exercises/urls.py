from django.urls import path
from apps.exercises import views

urlpatterns = [
    # Exercises
    path("exercises", views.ExerciseList.as_view(), name="exercise-list"),
    path("exercises/<int:pk>", views.ExerciseDetail.as_view(),
         name="exercise-detail"),

    # ExerciseLevels
    path("exercise-levels", views.ExerciseLevelList.as_view(),
         name="level-list"),
    path("exercise-levels/<int:pk>",
         views.ExerciseLevelDetail.as_view(), name="level-detail"),
]
