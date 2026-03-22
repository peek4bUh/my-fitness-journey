from django.urls import path

from apps.programs import views

urlpatterns = [
    path("programs/", views.ProgramList.as_view()),
    path("programs/<int:pk>/", views.ProgramDetail.as_view()),
]
