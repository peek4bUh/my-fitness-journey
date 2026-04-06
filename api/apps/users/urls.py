from django.urls import path

from apps.users import views


urlpatterns = [
    path("users", views.UserListView.as_view()),
    path("users/login", views.UserLoginView.as_view()),
    path("users/login/refresh", views.UserRefreshView.as_view()),
]
