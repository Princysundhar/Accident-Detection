# Generated by Django 3.2.20 on 2023-09-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accident', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='status',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
