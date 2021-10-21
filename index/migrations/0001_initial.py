# Generated by Django 3.2.8 on 2021-10-21 16:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import index.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Aviso', max_length=45)),
                ('contenido', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('img', models.ImageField(blank=True, max_length=256, null=True, upload_to=index.models.user_directory_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
