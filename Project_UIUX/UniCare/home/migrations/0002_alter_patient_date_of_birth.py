# Generated by Django 3.2.15 on 2022-08-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Date_of_Birth',
            field=models.CharField(max_length=10),
        ),
    ]
