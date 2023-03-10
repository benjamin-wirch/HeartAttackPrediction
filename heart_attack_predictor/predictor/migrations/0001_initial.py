# Generated by Django 4.1.1 on 2023-03-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('sex', models.BooleanField()),
                ('chest_pain', models.PositiveSmallIntegerField()),
                ('resting_blood_pressure', models.PositiveIntegerField()),
                ('serum_cholestrol', models.PositiveIntegerField()),
                ('fasting_blood_sugar', models.BooleanField()),
                ('resting_ecg', models.BooleanField()),
                ('max_heart_rate', models.PositiveIntegerField()),
                ('exercise_induced_angina', models.BooleanField()),
                ('fluoroscopy_count', models.PositiveSmallIntegerField()),
                ('thalassemia', models.PositiveSmallIntegerField()),
                ('predicted_risk', models.BooleanField(blank=True)),
                ('is_doctor', models.BooleanField(default=False)),
            ],
        ),
    ]
