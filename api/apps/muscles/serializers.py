from rest_framework import serializers

from apps.muscles.models import Muscle, MuscleGroup


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=C0115
        model = Muscle
        fields = "__all__"


class MuscleGroupSerializer(serializers.ModelSerializer):
    muscles = MuscleSerializer(many=True, read_only=True)

    class Meta:
        model = MuscleGroup
        fields = ['id', 'name', 'muscles', 'created_at']
