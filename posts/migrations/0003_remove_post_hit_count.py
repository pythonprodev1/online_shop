# Generated by Django 5.0 on 2024-01-01 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hit_count',
        ),
    ]
