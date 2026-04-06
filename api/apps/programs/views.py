# pylint: disable=no-member

from rest_framework import generics, status
from rest_framework.response import Response

from apps.programs.serializers import ProgramSerializer
from apps.programs.models import Program


class ProgramView(generics.GenericAPIView):
    """View for listing all programs."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def get(self, request, pk=None):
        """Retrieve programs for the authenticated user."""
        if pk:
            # Retrieve a specific program by ID, but only if it belongs to the user
            try:
                program = Program.objects.get(id=pk, user_id=request.user)
                serializer = self.get_serializer(program)
                return Response(serializer.data)
            except Program.DoesNotExist:
                return Response({"error": "Program not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # List all programs for the authenticated user
            programs = Program.objects.filter(user_id=request.user)
            serializer = self.get_serializer(programs, many=True)
            return Response(serializer.data)

    def post(self, request):
        """Create a new program."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgramDetailView(generics.GenericAPIView):
    """View for retrieving, creating, updating or deleting a program."""
    serializer_class = ProgramSerializer

    def get(self, request, program_id):
        """Retrieve a program by ID."""
        program = Program.objects.get(id=program_id)

        if program.user_id != request.user.id:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(program)
        return Response(serializer.data)

    def put(self, request):
        """Update an existing program."""
        program = self.get_object(pk)
        # Ensure the program belongs to the authenticated user
        if program.user_id != request.user:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        """Delete an existing program."""
        program = self.get_object(pk)
        # Ensure the program belongs to the authenticated user
        if program.user_id != request.user:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        program.delete()
        return Response(status=204)
