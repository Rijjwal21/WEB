# Generated by Django 3.2.15 on 2022-08-28 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_patient_blood_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Unique_ID',
        ),
    ]
