# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0004_auto_20161114_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name='hint',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checker.Task'),
        ),
    ]
