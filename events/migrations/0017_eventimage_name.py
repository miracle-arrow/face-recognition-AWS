# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-22 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_scanqueue'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimage',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
