from django.db import models

from apps.muscles.models import Muscle, MuscleGroup


class ExerciseLevel(models.Model):
    """Class representing an ExerciseLevel table."""
    class Meta:
        verbose_name_plural = "levels"
        db_table = "exercise_level"
        ordering = ["id"]

    name = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ExerciseForce(models.Model):
    class Meta:
        verbose_name_plural = "forces"
        db_table = "exercise_force"
        ordering = ['id']

    name = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ExerciseMechanic(models.Model):
    class Meta:
        verbose_name_plural = "mechanics"
        db_table = "exercise_mechanic"
        ordering = ['id']

    name = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ExerciseCategory(models.Model):
    class Meta:
        verbose_name_plural = "categories"
        db_table = "exercise_category"
        ordering = ['id']

    name = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ExerciseBodyRegion(models.Model):
    class Meta:
        verbose_name_plural = "body regions"
        db_table = "exercise_body_region"
        ordering = ['id']

    name = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    """Class representing an Exercise table."""
    class Meta:
        db_table = "exercise"

    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=255)
    target_muscle = models.ForeignKey(
        Muscle,
        on_delete=models.CASCADE,
        related_name="exercises",
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
    muscle_group = models.ForeignKey(
        MuscleGroup,
        on_delete=models.CASCADE,
        related_name="exercises",
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ExerciseInstruction(models.Model):
    class Meta:
        db_table = "exercise_instruction"

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name="instructions"
    )
    step = models.PositiveIntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.exercise.name} - Step {self.step}"


class ExerciseMuscle(models.Model):
    class Meta:
        db_table = "exercise_muscle"
        unique_together = ('exercise', 'muscle')
        ordering = ['role']

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
