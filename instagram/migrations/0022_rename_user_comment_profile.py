# Generated by Django 3.2.2 on 2021-05-21 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0021_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='profile',
        ),
    ]
