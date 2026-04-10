from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.exercises.serializers import ExerciseSerializer, DifficultySerializer
from apps.exercises.models import Exercise, Difficulty


class ExerciseList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDifficultyList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Difficulty.objects.all().order_by("id")
    serializer_class = DifficultySerializer


class ExerciseDifficultyDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
