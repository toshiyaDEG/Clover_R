# Generated by Django 3.2.8 on 2021-10-21 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aviso',
            old_name='img',
            new_name='imagen',
        ),
    ]
