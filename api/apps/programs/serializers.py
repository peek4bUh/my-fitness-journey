from rest_framework import serializers

from apps.programs.models import Program, ProgramSection, ProgramExercise


class ProgramSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = ["id", "user_id", "title", "description", "duration_weeks", "sections"]

    def get_sections(self, obj):
        sections = ProgramSection.objects.filter(program_id=obj)
        return ProgramSectionSerializer(sections, many=True).data


class ProgramSectionSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()

    class Meta:
        model = ProgramSection
        fields = ["id", "name", "program_id", "exercises"]

    def get_exercises(self, obj):
        exercises = ProgramExercise.objects.filter(section_id=obj)
        return ProgramExerciseSerializer(exercises, many=True).data


class ProgramExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramExercise
        fields = ["id", "name", "sets", "reps", "load", "rpe", "rest_seconds", "section_id"]