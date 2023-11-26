from django.db import models

# Create your models here.

class Timeline(models.Model):
    time = models.TimeField()
    description = models.TextField()