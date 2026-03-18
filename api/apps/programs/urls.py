from django.urls import path

from apps.programs import views

urlpatterns = [
    path("programs/", views.ProgramList.as_view()),
    path("programs/<int:pk>/", views.ProgramDetail.as_view()),
    path("programs/sections/", views.ProgramSectionList.as_view()),
    path("programs/sections/<int:pk>/", views.ProgramSectionDetail.as_view()),
    path("programs/exercises/", views.ProgramExerciseList.as_view()),
    path("programs/exercises/<int:pk>/", views.ProgramExerciseDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)