from rest_framework import serializers

from apps.programs.models import Program, ProgramSection, ProgramExercise
from apps.exercises.serializers import ExerciseSerializer


class ProgramExerciseSerializer(serializers.ModelSerializer):
    """Serializer for ProgramExercise model."""
    exercise = ExerciseSerializer(read_only=True)

    class Meta:  # pylint: disable=C0115
        model = ProgramExercise
        fields = ["id", "exercise", "sets", "reps", "load",
                  "rpe", "rest_seconds", "section_id"]


class ProgramSectionSerializer(serializers.ModelSerializer):
    """Serializer for ProgramSection model."""
    exercises = ProgramExerciseSerializer(many=True, read_only=True)

    class Meta:  # pylint: disable=C0115
        model = ProgramSection
        fields = ["id", "name", "program_id", "exercises"]


class ProgramSerializer(serializers.ModelSerializer):
    """Serializer for Program model."""
    owner = serializers.ReadOnlyField(source="owner.username")
    sections = ProgramSectionSerializer(many=True, read_only=True)

    class Meta:  # pylint: disable=C0115
        model = Program
        fields = ["id", "owner", "title",
                  "description", "duration_weeks", "sections"]
