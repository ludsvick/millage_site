# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20170601_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='municipality_millage',
            field=models.DecimalField(decimal_places=4, max_digits=7),
        ),
    ]