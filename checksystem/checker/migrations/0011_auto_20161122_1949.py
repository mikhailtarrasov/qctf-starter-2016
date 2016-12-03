# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0010_submit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='result_message',
            new_name='correct_flag_message',
        ),
        migrations.AddField(
            model_name='task',
            name='wrong_flag_message',
            field=models.TextField(default='Wrong flag'),
            preserve_default=False,
        ),
    ]
