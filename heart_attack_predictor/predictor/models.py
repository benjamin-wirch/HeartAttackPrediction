from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.PositiveSmallIntegerField(null=False)
    sex = models.BooleanField(null=False)
    chest_pain = models.PositiveSmallIntegerField(null=False)
    resting_blood_pressure = models.PositiveIntegerField(null=False)
