# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-27 23:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20180628_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pic',
        ),
    ]