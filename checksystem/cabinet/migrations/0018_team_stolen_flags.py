# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0017_auto_20161125_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='stolen_flags',
            field=models.IntegerField(default=0),
        ),
    ]
