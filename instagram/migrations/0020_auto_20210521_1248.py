# Generated by Django 3.2.2 on 2021-05-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0019_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
