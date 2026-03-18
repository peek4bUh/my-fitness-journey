from rest_framework import generics

from apps.programs.serializers import ProgramSerializer, ProgramSectionSerializer, ProgramExerciseSerializer
from apps.programs.models import Program, ProgramSection, ProgramExercise


class ProgramList(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ProgramSectionList(generics.ListCreateAPIView):
    serializer_class = ProgramSectionSerializer

    def get_queryset(self):
        queryset = ProgramSection.objects.all()
        program_id = self.request.query_params.get("program_id")
        if program_id is not None:
            queryset = queryset.filter(program_id=program_id)
        return queryset


class ProgramSectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProgramSection.objects.all()
    serializer_class = ProgramSectionSerializer


class ProgramExerciseList(generics.ListCreateAPIView):
    queryset = ProgramExercise.objects.all()
    serializer_class = ProgramExerciseSerializer


class ProgramExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProgramExercise.objects.all()
    serializer_class = ProgramExerciseSerializer
