# Generated by Django 2.2.6 on 2019-11-06 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SaudeMap', '0012_remove_fichadoenca_responsavelfamiliar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichadoenca',
            name='cnsresponsavelFamiliar',
        ),
        migrations.RemoveField(
            model_name='fichadoenca',
            name='dataNascimento',
        ),
        migrations.RemoveField(
            model_name='fichadoenca',
            name='microarea',
        ),
        migrations.RemoveField(
            model_name='fichadoenca',
            name='nomeCompleto',
        ),
        migrations.RemoveField(
            model_name='fichadoenca',
            name='nomeSocial',
        ),
    ]