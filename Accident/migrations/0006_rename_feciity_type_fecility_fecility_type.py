# Generated by Django 3.2.21 on 2023-09-26 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accident', '0005_rename_feciities_fecility_feciity_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fecility',
            old_name='feciity_type',
            new_name='fecility_type',
        ),
    ]
