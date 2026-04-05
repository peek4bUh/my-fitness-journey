from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.authentication.serializers import AuthLoginSerializer


@extend_schema(
    request=AuthLoginSerializer,
    responses={
        200: OpenApiResponse(
            response=AuthLoginSerializer,
            description="OK"
        )
    }
)
class AuthLoginView(generics.CreateAPIView):
    """View for API login."""
    serializer_class = AuthLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        """Authenticate user and return API key"""
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])

        if user is None:
            return Response({"detail": "Invalid credentials."},
                            status=status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.get(user=user)
        return Response({"api_key": token.key}, status=status.HTTP_200_OK)
