# Generated by Django 3.2.2 on 2021-05-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0009_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
