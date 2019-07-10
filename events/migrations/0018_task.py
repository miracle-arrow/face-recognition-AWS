# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-12 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0006_athlete_profile_complete'),
        ('events', '0017_eventimage_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletes.Athlete')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]
