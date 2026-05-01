from rest_framework import serializers

from apps.muscles.models import Muscle


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=C0115
        model = Muscle
        fields = ["id", "original", "english", "created_at"]
