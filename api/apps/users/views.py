from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.users.serializers import UserSerializer, UserCreateResponseSerializer


@extend_schema(
    responses={
        201: OpenApiResponse(
            description="Created",
            response=UserCreateResponseSerializer
        )
    },
    tags=["Users"],
)
class UserCreateView(generics.CreateAPIView):
    """View for creating a new user."""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({
            'message': 'User created successfully.'
        }, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Users"])
class UserRetrieveView(generics.RetrieveAPIView):
    """View for retrieving current user"""
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
