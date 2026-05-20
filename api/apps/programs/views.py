# pylint: disable=no-member

from rest_framework import generics, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.programs.serializers import ProgramSerializer, ProgramCreateResponseSerializer, ProgramUpdateResponseSerializer, ProgramDeleteResponseSerializer
from apps.programs.models import Program


@extend_schema(tags=["Programs"])
class ProgramListView(generics.GenericAPIView):
    """View for listing all programs."""
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def get(self, request):
        """Retrieve programs of the current user."""
        programs = Program.objects.filter(user_id=request.user)
        serializer = self.get_serializer(programs, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses={
            201: OpenApiResponse(
                description="Created",
                response=ProgramCreateResponseSerializer
            )
        },
        tags=["Programs"],
    )
    def post(self, request):
        """Create a new program."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response({
            'message': 'User created successfully.'
        }, status=status.HTTP_201_CREATED)


@extend_schema(
    tags=["Programs"],
)
class ProgramDetailView(generics.GenericAPIView):
    """View for retrieving, creating, updating or deleting a program."""
    serializer_class = ProgramSerializer

    def get(self, request, pk):
        """Retrieve a program by ID."""
        program = Program.objects.get(id=pk)

        if program.user_id != request.user.id:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(program)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

    @extend_schema(
        responses={
            200: OpenApiResponse(
                description="OK",
                response=ProgramUpdateResponseSerializer
            )
        },
        tags=["Programs"],
    )
    def put(self, request, pk):
        """Update an existing program."""
        program = self.get_object(pk)
        if program.user_id != request.user:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(program, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message': 'User updated successfully.'
        }, status=status.HTTP_200_OK)

    @extend_schema(
        responses={
            200: OpenApiResponse(
                description="OK",
                response=ProgramDeleteResponseSerializer
            )
        },
        tags=["Programs"],
    )
    def delete(self, request, pk):
        """Delete an existing program."""
        program = self.get_object(pk)
        if program.user_id != request.user:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        program.delete()
        return Response({
            'message': 'User deleted successfully.'
        }, status=status.HTTP_200_OK)
