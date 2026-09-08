from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path("workouts/", views.workouts_index, name="workouts_index"),
    path("exercises/", views.exercises_index, name="exercises_index"),
]
