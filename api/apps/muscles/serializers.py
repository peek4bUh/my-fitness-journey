from rest_framework import serializers

from apps.muscles.models import Muscle, MuscleGroup, MuscleHead


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=C0115
        model = Muscle
        fields = ['id', 'original', 'english']


class MuscleGroupSerializer(serializers.ModelSerializer):
    muscles = MuscleSerializer(many=True, read_only=True)

    class Meta:
        model = MuscleGroup
        fields = ['id', 'name', 'muscles', 'created_at']


class MuscleHeadSerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=C0115
        model = MuscleHead
        fields = ['id', 'name']
