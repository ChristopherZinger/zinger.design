# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-19 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='duration',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='endDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='startDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='level_dec',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level_procentage',
            field=models.IntegerField(default=0),
        ),
    ]
