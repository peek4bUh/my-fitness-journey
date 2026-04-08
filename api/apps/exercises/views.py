from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from apps.exercises.serializers import ExerciseSerializer
from apps.exercises.models import Exercise


class ExerciseList(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
