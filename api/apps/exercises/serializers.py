from rest_framework import serializers

from apps.exercises.models import Exercise, ExerciseLevel, ExerciseMuscle, ExerciseMuscle
from apps.muscles.serializers import MuscleSerializer


class ExerciseLevelSerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=C0115
        model = ExerciseLevel
        exclude = ["created_at"]


class ExerciseSerializer(serializers.ModelSerializer):
    level = serializers.ReadOnlyField(source='level.name')
    target_muscle = MuscleSerializer(read_only=True)
    secondary_muscles = serializers.SerializerMethodField()
    tertiary_muscles = serializers.SerializerMethodField()

    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'description',
            'level',
            'force',
            'mechanic',
            'body_region',
            'category',
            'target_muscle',
            'secondary_muscles',
            'tertiary_muscles',
        ]

    def get_secondary_muscles(self, obj):
        secondaries = obj.exercise_muscles.filter(
            role=ExerciseMuscle.MuscleRole.SECONDARY
        ).select_related('muscle')
        return MuscleSerializer(
            [em.muscle for em in secondaries], many=True
        ).data

    def get_tertiary_muscles(self, obj):
        tertiaries = obj.exercise_muscles.filter(
            role=ExerciseMuscle.MuscleRole.TERTIARY
        ).select_related('muscle')
        return MuscleSerializer(
            [em.muscle for em in tertiaries], many=True
        ).data
