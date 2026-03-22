from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    class Meta:  # pylint: disable=C0115
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
