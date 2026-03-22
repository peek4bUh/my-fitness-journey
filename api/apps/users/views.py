from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework.response import Response
from rest_framework import generics, authentication, status

from apps.users.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]


class UserLogin(generics.CreateAPIView):
    """View for user login."""
    serializer_class = UserSerializer

    def post(self, request, format=None):
        """Authenticate user and return token."""
        user = User.objects.filter(
            username=request.data.get("username")).first()

        if user is None:
            return Response({"detail": "User not found."},
                            status=status.HTTP_404_NOT_FOUND)

        if user.email != request.data.get("email") \
                or not check_password(request.data.get("password"), user.password):
            return Response({"detail": "Invalid credentials."},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Implement login logic here
        return Response({"token": "TOKEN_PLACEHOLDER"}, status=status.HTTP_200_OK)
