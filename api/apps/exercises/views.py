from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.exercises.serializers import ExerciseSerializer
from apps.exercises.models import Exercise


class ExerciseList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
