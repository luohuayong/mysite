# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_auto_20171105_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='danjia',
            field=models.FloatField(null=True, verbose_name='单价'),
        ),
        migrations.AddField(
            model_name='huxing',
            name='danjia',
            field=models.FloatField(null=True, verbose_name='单价'),
        ),
        migrations.AddField(
            model_name='pian',
            name='danjia',
            field=models.FloatField(null=True, verbose_name='单价'),
        ),
        migrations.AddField(
            model_name='qu',
            name='danjia',
            field=models.FloatField(null=True, verbose_name='单价'),
        ),
        migrations.AddField(
            model_name='xiaoqu',
            name='danjia',
            field=models.FloatField(null=True, verbose_name='单价'),
        ),
        migrations.AddField(
            model_name='xuexiao',
            name='danjia',
            field=models.FloatField(null=True, verbose_name='单价'),
        ),
    ]
