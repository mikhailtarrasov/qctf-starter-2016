# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0002_team_tasks_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='tasks_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
