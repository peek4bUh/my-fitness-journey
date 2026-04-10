from rest_framework import serializers

from apps.exercises.models import Difficulty, Exercise


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=C0115
        model = Difficulty
        fields = ["id", "name"]


class ExerciseSerializer(serializers.ModelSerializer):
    difficulty = DifficultySerializer(read_only=True)
    difficulty_id = serializers.PrimaryKeyRelatedField(
        queryset=Difficulty.objects.all(),
        source="difficulty",
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:  # pylint: disable=C0115
        model = Exercise
        fields = ["id", "name", "difficulty", "difficulty_id", "created"]
