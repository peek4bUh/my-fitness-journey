from django.urls import path

from apps.users import views


urlpatterns = [
    path("users", views.UserCreateView.as_view()),
    path("users/me", views.UserRetrieveView.as_view()),
]
