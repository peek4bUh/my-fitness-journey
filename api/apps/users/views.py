from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.serializers import UserSerializer


class UserListView(generics.GenericAPIView):
    """View for listing current user or creating a new user."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return super().get_permissions()

    def get(self, request):
        """Return the info of the current user."""
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        token = auth_header.split(' ')[1]
        access_token = AccessToken(token)
        user_id = access_token['user_id']
        serializer = self.get_serializer(User.objects.get(id=user_id))

        return Response(serializer.data)

    def post(self, request):
        """Create a new user."""
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(TokenObtainPairView):
    """View for authenticate an user and return a JWT token."""
    permission_classes = [AllowAny]


class UserRefreshView(TokenRefreshView):
    """View for refreshing JWT tokens."""
    permission_classes = [AllowAny]
