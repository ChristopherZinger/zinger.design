# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-22 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20180722_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='duration',
            field=models.DateField(blank=True, null=True),
        ),
    ]