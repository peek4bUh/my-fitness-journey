from django.db import models
from django.contrib.auth.models import User

from apps.exercises.models import Exercise


class Program(models.Model):
    """Class representing a Program model"""
    user = models.ForeignKey(
        to=User,
        related_name="programs",
        on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name="Program title", max_length=128)
    description = models.CharField(
        verbose_name="Program description", max_length=255)
    created_at = models.DateTimeField(
        verbose_name="Creation date", auto_now_add=True)

    def __repr__(self):
        return super().__repr__()


class ProgramSection(models.Model):
    """Class representing a ProgramSection model"""
    program = models.ForeignKey(
        to=Program,
        related_name="sections",
        on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name="Section name", max_length=100)
    created_at = models.DateTimeField(
        verbose_name="Creation date", auto_now_add=True)


class ProgramExercise(models.Model):
    """Class representing a ProgramExercise model"""
    section = models.ForeignKey(
        to=ProgramSection,
        related_name="exercises",
        on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        to=Exercise,
        on_delete=models.CASCADE
    )
    sets = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    load = models.FloatField(null=True, blank=True)
    rpe = models.PositiveSmallIntegerField()
    rest_seconds = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
