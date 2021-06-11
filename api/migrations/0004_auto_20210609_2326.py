# Generated by Django 3.2.4 on 2021-06-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210609_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.AddField(
            model_name='photo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='has_face',
            field=models.BooleanField(default=False),
        ),
    ]