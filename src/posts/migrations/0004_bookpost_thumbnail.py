# Generated by Django 4.0.1 on 2022-03-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_bookpost_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
