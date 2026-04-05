from django.urls import path

from apps.users import views


urlpatterns = [
    path("users", views.UserList.as_view()),
    path("users/<int:pk>", views.UserDetail.as_view()),
    path("users/login", views.UserLoginView.as_view()),
    # path("users/logout", views.UserDetail.as_view()),
    # path("users/password_change", views.UserDetail.as_view()),
    # path("users/password_reset", views.UserDetail.as_view()),
]
