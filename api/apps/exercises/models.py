from django.db import models

from apps.muscles.models import Muscle


class ExerciseLevel(models.Model):
    """Class representing an ExerciseLevel table."""
    class Meta:
        verbose_name_plural = "levels"
        db_table = "exercise_level"
        ordering = ["id"]

    name = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ExerciseForce(models.Model):
    class Meta:
        db_table = "exercise_force"

    name = models.CharField(max_length=32, unique=True)


class ExerciseMechanic(models.Model):
    class Meta:
        db_table = "exercise_mechanic"

    name = models.CharField(max_length=32, unique=True)


class ExerciseCategory(models.Model):
    class Meta:
        db_table = "exercise_category"

    name = models.CharField(max_length=32, unique=True)


class ExerciseBodyRegion(models.Model):
    class Meta:
        db_table = "exercise_body_region"

    name = models.CharField(max_length=32, unique=True)


class Exercise(models.Model):
    """Class representing an Exercise table."""
    class Meta:
        db_table = "exercise"

    # class ExerciseForce(models.TextChoices):
    #     PUSH = 'Push'
    #     PULL = 'Pull'
    #     HOLD = 'Hold'

    # class ExerciseBodyRegion(models.TextChoices):
    #     CORE = 'Core'
    #     FULL_BODY = 'Full Body'
    #     LOWER_BODY = 'Lower Body'
    #     UPPER_BODY = 'Upper Body'

    # class ExerciseCategory(models.TextChoices):
    #     BALANCE = 'Balance'
    #     BODYBUILDING = 'Bodybuilding'
    #     CALISTHENICS = 'Calisthenics'
    #     MOBILITY = 'Mobility'
    #     POSTURAL = 'Postural'

    name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    description = models.CharField(max_length=255, null=False)
    target_muscle = models.ForeignKey(
        Muscle,
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )
    level = models.ForeignKey(
        ExerciseLevel,
        on_delete=models.CASCADE,
        related_name="exercises",
        default=1
    )
    force = models.ForeignKey(
        ExerciseForce,
        on_delete=models.CASCADE,
        related_name="exercises",
        default=1
    )
    mechanic = models.ForeignKey(
        ExerciseMechanic,
        on_delete=models.CASCADE,
        related_name="exercises",
        default=1
    )
    body_region = models.ForeignKey(
        ExerciseBodyRegion,
        on_delete=models.CASCADE,
        related_name="exercises",
        default=1
    )
    category = models.ForeignKey(
        ExerciseCategory,
        on_delete=models.CASCADE,
        related_name="exercises",
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ExerciseMuscle(models.Model):
    class Meta:
        db_table = "exercise_muscle"
        unique_together = ('exercise', 'muscle')
        ordering = ['role', 'order']

    class MuscleRole(models.TextChoices):
        SECONDARY = 'secondary'
        TERTIARY = 'tertiary'

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='exercise_muscles'
    )
    muscle = models.ForeignKey(
        Muscle,
        on_delete=models.CASCADE,
        related_name='muscle_exercises'
    )
    role = models.CharField(
        max_length=20,
        choices=MuscleRole.choices,
    )
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
