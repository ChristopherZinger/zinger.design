# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-13 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20180911_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgorder',
            name='img',
        ),
        migrations.AddField(
            model_name='projectimg',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='ImgOrder',
        ),
    ]
