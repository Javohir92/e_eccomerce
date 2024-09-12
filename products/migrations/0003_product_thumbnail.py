# Generated by Django 5.0.3 on 2024-07-04 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('products', '0002_productimage_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.media'),
        ),
    ]
