
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


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserLoginView(TokenObtainPairView):
    """View for authenticate an user and return a JWT token."""
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        user = authenticate(username=request.data.get('username', None),
                            password=request.data.get('password', None))

        if user is None:
            return Response({"Invalid": "Invalid username or password!!"},
                            status=status.HTTP_404_NOT_FOUND)

        data = get_tokens_for_user(user)

        response = Response(data=data)
        response.set_cookie(
            key='access_token',
            value=data["access"],
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            samesite='None',
            secure=True,
            httponly=True
        )

        response.set_cookie(
            key='refresh_token',
            value=data["refresh"],
            expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            samesite='None',
            secure=True,
            httponly=True
        )

        return response


class UserRefreshView(TokenRefreshView):
    """View for refreshing JWT tokens."""
    permission_classes = [AllowAny]


class UserLogoutView(generics.GenericAPIView):
    """View for logging out a user by clearing JWT cookies."""
    permission_classes = [AllowAny]

    def post(self, request):
        response = Response({"message": "Successfully logged out"})
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response
