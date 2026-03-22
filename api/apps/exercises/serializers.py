from rest_framework import serializers

from apps.exercises.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=C0115
        model = Exercise
        fields = ["id", "title"]
