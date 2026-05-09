from django.urls import path

from apps.muscles import views


urlpatterns = [
    # Muscles
    path("muscles", views.MuscleList.as_view(), name="muscle-list"),
    path("muscles/<int:pk>", views.MuscleDetail.as_view(), name="muscle-detail"),

    # Muscle Groups
    path("muscle-groups", views.MuscleGroupList.as_view(),
         name="muscle-group-list"),
    path("muscle-groups/<int:pk>", views.MuscleGroupDetail.as_view(),
         name="muscle-group-detail"),
]
