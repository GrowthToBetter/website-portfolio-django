# Generated by Django 5.1.3 on 2024-11-27 19:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_myproject_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproject',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
