from django.db import models

from apps.users.models import User


class Program(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    duration_weeks = models.IntegerField()


class ProgramSection(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    program_id = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)


class ProgramExercise(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    section_id = models.ForeignKey(
        ProgramSection,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    load = models.FloatField(null=True, blank=True)
    rpe = models.IntegerField()
    rest_seconds = models.IntegerField(null=True, blank=True)
