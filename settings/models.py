from django.db import models

# Create your models here.

class Effect(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=5, default=0)
    param = models.IntegerField(default=0)

class Twitter(models.Model):
    status = models.CharField(max_length=5, default=0)
    modifier = models.IntegerField(default=0)
