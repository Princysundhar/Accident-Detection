# Generated by Django 3.2.21 on 2023-09-30 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accident', '0006_rename_feciity_type_fecility_fecility_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='police_station',
            name='lattitude',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='police_station',
            name='longitude',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
