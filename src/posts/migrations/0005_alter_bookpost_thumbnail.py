# Generated by Django 4.0.1 on 2022-03-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_bookpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='book'),
        ),
    ]
