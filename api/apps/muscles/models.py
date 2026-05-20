from django.db import models


class Muscle(models.Model):
    """Class representing a Muscle table."""
    class Meta:
        ordering = ["original"]
        db_table = "muscle"

    original = models.CharField(max_length=128, unique=True, null=False)
    english = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original


class MuscleGroup(models.Model):
    """Class representing a Muscle Group table."""
    class Meta:
        ordering = ["name"]
        db_table = "muscle_group"
        verbose_name = "Muscle Group"
        verbose_name_plural = "Muscle Groups"

    name = models.CharField(max_length=64, unique=True)
    muscles = models.ManyToManyField(
        Muscle,
        related_name='groups',
        through='MuscleGroupMuscle'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MuscleGroupMuscle(models.Model):
    muscle = models.ForeignKey(Muscle, on_delete=models.CASCADE)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "muscle_group_muscle"
        unique_together = ('muscle', 'muscle_group')


class MuscleHead(models.Model):
    """Class representing a Muscle Head table."""
    class Meta:
        ordering = ["name"]
        db_table = "muscle_head"
        verbose_name = "Muscle Head"
        verbose_name_plural = "Muscle Heads"

    name = models.CharField(max_length=64)
    muscle = models.ForeignKey(
        Muscle, on_delete=models.CASCADE, related_name='heads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.muscle.original} - {self.name}"
