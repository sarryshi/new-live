# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20170320_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetail',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='rating_sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='sub_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
