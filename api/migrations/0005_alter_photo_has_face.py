# Generated by Django 3.2.4 on 2021-06-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210609_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='has_face',
            field=models.BooleanField(default=True),
        ),
    ]
