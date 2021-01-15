from django.db import models


class Plant(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
