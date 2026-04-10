
from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from config import settings

from apps.users.serializers import UserSerializer


class UserListView(generics.GenericAPIView):
    """View for listing current user or creating a new user."""
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return super().get_permissions()

    def get(self, request):
        """Return the info of the current user."""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def post(self, request):
        """Create a new user."""
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
