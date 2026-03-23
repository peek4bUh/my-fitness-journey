from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework.response import Response
from rest_framework import generics, authentication, status
from rest_framework.authtoken.models import Token

from apps.users.serializers import UserSerializer, LoginSerializer


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


class UserLogin(generics.CreateAPIView):
    """View for user login."""
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        """Authenticate user and return token."""
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = User.objects.filter(username=username).first()

        if user is None or not check_password(password, user.password):
            return Response({"detail": "Invalid credentials."},
                            status=status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.get(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
