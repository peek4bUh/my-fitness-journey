# pylint: disable=no-member

from rest_framework import generics
from rest_framework.response import Response

from apps.programs.serializers import ProgramSerializer, ProgramSectionSerializer, ProgramExerciseSerializer
from apps.programs.models import Program, ProgramSection, ProgramExercise


class ProgramList(generics.ListAPIView):
    """View for listing all programs."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProgramDetail(generics.GenericAPIView):
    """View for retrieving, creating, updating or deleting a program."""
    # TODO: TEST this

    def get(self, request, pk=None, format=None):
        """Retrieve a program by ID."""
        program = self.get_object(pk)
        serializer = self.get_serializer(program)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a new program."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk=None, format=None):
        """Update an existing program."""
        program = self.get_object(pk)
        serializer = self.get_serializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None, format=None):
        """Delete a program."""
        program = self.get_object(pk)
        program.delete()
        return Response(status=204)

    # queryset = Program.objects.all()
    # serializer_class = ProgramSerializer


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
