from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.exercises.serializers import ExerciseSerializer
from apps.exercises.models import Exercise


class ExerciseList(ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
