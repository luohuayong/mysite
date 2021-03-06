# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('first', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('two', '\u4e24\u53a2'), ('three', '\u4e09\u53a2'), ('sport', '\u8dd1\u8f66'), ('suv', 'SUV'), ('mpv', 'MPV'), ('pickup', '\u76ae\u5361'), ('van', '\u9762\u5305\u8f66'), ('other', '\u5176\u4ed6')], max_length=10)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price_new', models.DecimalField(decimal_places=2, max_digits=5)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Province'),
        ),
    ]
