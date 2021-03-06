# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-22 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0007_auto_20180722_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='no_graph',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='point_graph',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='time_graph',
        ),
        migrations.AddField(
            model_name='skillgroup',
            name='no_graph',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='skillgroup',
            name='point_graph',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='skillgroup',
            name='time_graph',
            field=models.BooleanField(default=False),
        ),
    ]
