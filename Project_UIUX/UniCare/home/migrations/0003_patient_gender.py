# Generated by Django 3.2.15 on 2022-08-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_patient_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Gender',
            field=models.CharField(default='Select', max_length=10),
        ),
    ]
