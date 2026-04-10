from django.urls import path

from apps.users import views


urlpatterns = [
    path("users", views.UserListView.as_view()),
]
