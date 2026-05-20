from rest_framework import serializers

from apps.programs.models import Program, ProgramSection, ProgramExercise
from apps.exercises.models import Exercise
from apps.exercises.serializers import ExerciseSerializer


class ProgramExerciseSerializer(serializers.ModelSerializer):
    """Serializer for ProgramExercise model."""
    exercise = ExerciseSerializer(read_only=True)
    exercise_id = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(),
        write_only=True,
        source="exercise"
    )

    class Meta:  # pylint: disable=C0115
        model = ProgramExercise
        fields = [
            "id",
            "exercise",
            "exercise_id",
            "sets",
            "reps",
            "load",
            "rpe",
            "rest_seconds"
        ]
        extra_kwargs = {
            'sets': {'default': 0},
            'reps': {'default': 0},
            'rpe': {'default': 0},
            'rest_seconds': {'default': 0},
        }

    def create(self, validated_data):
        return ProgramExercise.objects.create(**validated_data)


class ProgramSectionSerializer(serializers.ModelSerializer):
    """Serializer for ProgramSection model."""
    data = ProgramExerciseSerializer(many=True, source="exercises")

    class Meta:  # pylint: disable=C0115
        model = ProgramSection
        fields = ["id", "name", "data"]

    def create(self, validated_data):
        exercises_data = validated_data.pop("exercises", [])
        program = validated_data.pop("program")

        section = ProgramSection.objects.create(
            program=program,
            **validated_data
        )

        for exercise_data in exercises_data:
            ProgramExercise.objects.create(
                section=section,
                **exercise_data
            )

        return section


class ProgramSerializer(serializers.ModelSerializer):
    """Serializer for Program model."""
    sections = ProgramSectionSerializer(many=True)

    class Meta:  # pylint: disable=C0115
        model = Program
        fields = ["id", "title", "description",  "sections"]

    def create(self, validated_data):
        sections_data = validated_data.pop("sections", [])
        program = Program.objects.create(**validated_data)

        for section_data in sections_data:
            exercises_data = section_data.pop("exercises", [])

            section = ProgramSection.objects.create(
                program=program,
                **section_data
            )

            for exercise_data in exercises_data:
                ProgramExercise.objects.create(
                    section=section,
                    **exercise_data
                )

        return program


class ProgramCreateResponseSerializer(serializers.Serializer):
    message = serializers.CharField(default='Program created successfully.')


class ProgramUpdateResponseSerializer(serializers.Serializer):
    message = serializers.CharField(default='Program updated successfully.')


class ProgramDeleteResponseSerializer(serializers.Serializer):
    message = serializers.CharField(default='Program deleted successfully.')
