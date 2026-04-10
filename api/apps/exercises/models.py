from django.db import models


class Difficulty(models.Model):
    """Class representing an Exercise difficulty level."""
    name = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Exercise(models.Model):
    """Class representing an Exercise model."""
    name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    difficulty = models.ForeignKey(
        Difficulty,
        on_delete=models.CASCADE,
        related_name="exercises",
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
