from django.urls import path

from apps.programs import views

urlpatterns = [
    path("programs", views.ProgramView.as_view()),
    path("programs/<int:program_id>", views.ProgramDetailView.as_view()),
]
