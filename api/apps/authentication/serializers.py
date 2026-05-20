from rest_framework import serializers


class AuthLoginSerializer(serializers.Serializer):
    """Serializer for API login."""
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    api_key = serializers.CharField(read_only=True)


class LoginAccessTokenResponseSerializer(serializers.Serializer):
    access = serializers.CharField(default='string')
