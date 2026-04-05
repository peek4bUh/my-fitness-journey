from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    """View for listing all users or creating a new user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        """Return a list of all users."""
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a new user."""
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, or deleting a user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(TokenObtainPairView):
    """View for authenticate an user and return a JWT token."""
    permission_classes = [AllowAny]
