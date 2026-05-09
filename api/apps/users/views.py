from rest_framework import generics
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from apps.users.serializers import UserSerializer


@extend_schema(tags=["Users"])
class UserCreateView(generics.CreateAPIView):
    """View for creating a new user."""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=["Users"])
class UserRetrieveView(generics.RetrieveAPIView):
    """View for retrieving current user"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return self.request.user
