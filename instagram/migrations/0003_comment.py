# Generated by Django 3.2.2 on 2021-05-18 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20210518_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instagram.image')),
                ('profile', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instagram.profile')),
            ],
        ),
    ]
