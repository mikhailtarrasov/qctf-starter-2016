# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0016_hint_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='price',
            field=models.IntegerField(),
        ),
    ]
