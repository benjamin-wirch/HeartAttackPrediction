from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, blank=True, null=True)

    age = models.PositiveSmallIntegerField(null=True, blank=True)

    sex = models.BooleanField(null=True, blank=True)

    chest_pain = models.PositiveSmallIntegerField(null=True, blank=True)

    resting_blood_pressure = models.PositiveIntegerField(
        null=True, blank=True)

    serum_cholestrol = models.PositiveIntegerField(null=True, blank=True)

    fasting_blood_sugar = models.BooleanField(null=True, blank=True)

    resting_ecg = models.BooleanField(null=True, blank=True)

    max_heart_rate = models.PositiveIntegerField(null=True, blank=True)

    exercise_induced_angina = models.BooleanField(null=True, blank=True)

    fluoroscopy_count = models.PositiveSmallIntegerField(
        null=True, blank=True)

    thalassemia = models.PositiveSmallIntegerField(null=True, blank=True)

    predicted_risk = models.BooleanField(null=True, blank=True)

    is_doctor = models.BooleanField(null=True, default=False, blank=True)

    def __repr__(self):
        return self.name if self.name else super().__repr__(self)

    def __str__(self):
        return self.name if self.name else super().__str__(self)
