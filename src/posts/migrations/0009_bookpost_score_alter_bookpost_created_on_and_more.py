# Generated by Django 4.0.1 on 2022-03-08 16:04

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_bookrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpost',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='bookpost',
            name='created_on',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='bookrating',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Note'),
        ),
    ]
