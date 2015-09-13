from django.db import models

# Create your models here.
class Effect(models.Model):
    effect_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    param_val = models.IntegerField(default=0)

    def __str__(self):
        return self.effect_name
