# Generated by Django 2.2.3 on 2019-11-13 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SaudeMap', '0037_auto_20191113_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichadoenca',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='fichadoenca',
            name='longitude',
        ),
    ]
