# Generated by Django 3.2.15 on 2022-11-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_document_uniqueid'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='Email',
            field=models.EmailField(max_length=30, null=True),
        ),
    ]
