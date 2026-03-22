from django.db import models


class Program(models.Model):
    """Class representing a Program model"""
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        "auth.User",
        related_name="programs",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    duration_weeks = models.SmallIntegerField()


class ProgramSection(models.Model):
    """Class representing a ProgramSection model"""
    class Meta:  # pylint: disable=C0115
        db_table = "programs_program_sections"

    created = models.DateTimeField(auto_now_add=True)
    program_id = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)


class ProgramExercise(models.Model):
    """Class representing a ProgramExercise model"""
    class Meta:  # pylint: disable=C0115
        db_table = "programs_program_exercises"

    created = models.DateTimeField(auto_now_add=True)
    section_id = models.ForeignKey(
        ProgramSection,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    sets = models.SmallIntegerField()
    reps = models.SmallIntegerField()
    load = models.FloatField(null=True, blank=True)
    rpe = models.SmallIntegerField()
    rest_seconds = models.SmallIntegerField(null=True, blank=True)
