# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tasks_number',
            field=models.IntegerField(default=0),
        ),
    ]
