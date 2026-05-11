from rest_framework import serializers

from apps.exercises.models import Exercise, ExerciseInstruction, ExerciseLevel, ExerciseMuscle, ExerciseMuscle
from apps.muscles.serializers import MuscleSerializer


class ExerciseLevelSerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=C0115
        model = ExerciseLevel
        exclude = ["created_at"]


class ExerciseSerializer(serializers.ModelSerializer):
    level = serializers.ReadOnlyField(source='level.name')
    force = serializers.ReadOnlyField(source='force.name')
    mechanic = serializers.ReadOnlyField(source='mechanic.name')
    body_region = serializers.ReadOnlyField(source='body_region.name')
    muscle_group = serializers.ReadOnlyField(source='muscle_group.name')
    category = serializers.ReadOnlyField(source='category.name')
    target_muscle = serializers.ReadOnlyField(source='target_muscle.original')
    secondary_muscles = serializers.SerializerMethodField()
    tertiary_muscles = serializers.SerializerMethodField()
    instructions = serializers.SerializerMethodField()

    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'description',
            'level',
            'force',
            'mechanic',
            'category',
            'body_region',
            'muscle_group',
            'target_muscle',
            'secondary_muscles',
            'tertiary_muscles',
            'instructions',
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

    def get_instructions(self, obj):
        return list(obj.instructions.order_by('step').values_list('description', flat=True))
