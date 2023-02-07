# Generated by Django 4.1.3 on 2023-01-14 16:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='video'),
        ),
    ]