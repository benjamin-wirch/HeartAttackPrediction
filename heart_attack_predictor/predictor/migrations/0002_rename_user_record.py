# Generated by Django 4.1.1 on 2023-03-05 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Record',
        ),
    ]
