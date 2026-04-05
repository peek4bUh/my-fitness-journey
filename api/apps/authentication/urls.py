from django.urls import path

from apps.authentication import views

urlpatterns = [
    path("auth/login", views.AuthLoginView.as_view()),
]
