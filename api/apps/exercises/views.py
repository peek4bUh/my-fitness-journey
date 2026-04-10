from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from apps.exercises.serializers import ExerciseSerializer, DifficultySerializer
from apps.exercises.models import Exercise, Difficulty


class ExerciseList(ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()


class ExerciseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()


class ExerciseDifficultyList(ListCreateAPIView):
    queryset = Difficulty.objects.all().order_by("id")
    serializer_class = DifficultySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()


class ExerciseDifficultyDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()
