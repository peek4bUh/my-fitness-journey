from django.db import models


class Exercise(models.Model):
    """Class representing an Exercise model"""
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
