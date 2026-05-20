from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    class Meta:  # pylint: disable=C0115
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {
            'username': {'default': 'string'},
            'email': {'default': 'string'},
            "password": {"write_only": True, 'default': 'string'},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)
        return user


class UserCreateResponseSerializer(serializers.Serializer):
    message = serializers.CharField(default='User created successfully.')
