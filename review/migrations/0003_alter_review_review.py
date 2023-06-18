# Generated by Django 3.2 on 2023-06-18 03:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
    ]