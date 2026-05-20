from django.urls import path

from apps.programs import views

urlpatterns = [
    path("programs", views.ProgramListView.as_view(), name="program-list"),
    path("programs/<int:pk>", views.ProgramDetailView.as_view(),
         name="program-detail"),
]
