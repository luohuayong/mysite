# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0008_auto_20171109_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='caiji',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
    ]
