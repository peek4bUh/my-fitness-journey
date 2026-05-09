from rest_framework.generics import ListAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from apps.exercises.serializers import ExerciseSerializer, ExerciseLevelSerializer
from apps.exercises.models import Exercise, ExerciseLevel


@extend_schema(tags=["Exercises"])
class ExerciseList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Exercise.objects.select_related('target_muscle').prefetch_related(
        'exercise_muscles__muscle'
    ).all()
    serializer_class = ExerciseSerializer


@extend_schema(tags=["Exercises"])
class ExerciseDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Exercise.objects.select_related('target_muscle').prefetch_related(
        'exercise_muscles__muscle'
    ).all()
    serializer_class = ExerciseSerializer


@extend_schema(tags=["Exercise Levels"])
class ExerciseLevelList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = ExerciseLevel.objects.all()
    serializer_class = ExerciseLevelSerializer


@extend_schema(tags=["Exercise Levels"])
class ExerciseLevelDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = ExerciseLevel.objects.all()
    serializer_class = ExerciseLevelSerializer
