# Generated by Django 3.2.15 on 2022-11-18 18:05

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_document_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='DDate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='DName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Images',
            field=models.FileField(blank='true', upload_to=home.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='document',
            name='Images',
            field=models.FileField(blank='true', upload_to='images'),
        ),
    ]
