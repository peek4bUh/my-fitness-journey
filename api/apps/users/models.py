from django.db import models


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=255, unique=True)

    