# Generated by Django 4.1.1 on 2023-03-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0006_alter_record_age_alter_record_chest_pain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='predicted_risk',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
