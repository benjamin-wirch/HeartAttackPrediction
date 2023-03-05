# Generated by Django 4.1.1 on 2023-03-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0004_alter_record_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='chest_pain',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='exercise_induced_angina',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='fasting_blood_sugar',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='fluoroscopy_count',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='is_doctor',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='record',
            name='max_heart_rate',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='resting_blood_pressure',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='resting_ecg',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='serum_cholestrol',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='sex',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='thalassemia',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]