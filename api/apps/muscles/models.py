from django.db import models

# Create your models here.


class Muscle(models.Model):
    """Class representing a Muscle model."""
    original = models.CharField(max_length=128, unique=True, null=False)
    english = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original
