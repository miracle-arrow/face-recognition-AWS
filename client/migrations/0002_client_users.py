# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-30 20:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='users',
            field=models.ManyToManyField(related_name='project_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
