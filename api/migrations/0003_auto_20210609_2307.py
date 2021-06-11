# Generated by Django 3.2.4 on 2021-06-09 23:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_photo_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=cloudinary.models.CloudinaryField(default=0, max_length=255, verbose_name='image'),
        ),
    ]