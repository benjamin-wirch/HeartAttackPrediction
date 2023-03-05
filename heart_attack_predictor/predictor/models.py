from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, blank=False, null=False)

    age = models.PositiveSmallIntegerField(null=False)

    sex = models.BooleanField(null=False)

    chest_pain = models.PositiveSmallIntegerField(null=False)

    resting_blood_pressure = models.PositiveIntegerField(null=False)

    serum_cholestrol = models.PositiveIntegerField(null=False)

    fasting_blood_sugar = models.BooleanField(null=False)

    resting_ecg = models.BooleanField(null=False)

    max_heart_rate = models.PositiveIntegerField(null=False)

    exercise_induced_angina = models.BooleanField(null=False)

    fluoroscopy_count = models.PositiveSmallIntegerField(null=False)

    thalassemia = models.PositiveSmallIntegerField(null=False)

    predicted_risk = models.BooleanField(blank=True)

    is_doctor = models.BooleanField(null=False, default=False)
