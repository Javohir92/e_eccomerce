# Generated by Django 5.0.3 on 2024-09-11 12:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_country_options_alter_media_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourinstagramstory',
            name='story_link',
            field=models.URLField(validators=[django.core.validators.URLValidator()], verbose_name='Story_link'),
        ),
    ]
