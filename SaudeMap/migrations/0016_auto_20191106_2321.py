# Generated by Django 2.2.6 on 2019-11-07 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SaudeMap', '0015_auto_20191106_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichadoenca',
            name='cnsResponsavelFamiliar',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='fichadoenca',
            name='microArea',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
