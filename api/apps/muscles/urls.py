from django.urls import path

from apps.muscles import views


urlpatterns = [
    path("muscles", views.MuscleList.as_view(), name="muscle-list"),
]
