# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county_name', models.CharField(max_length=75)),
                ('county_millage', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=100)),
                ('district_millage', models.DecimalField(decimal_places=4, max_digits=6)),
                ('district_county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.District')),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipality_name', models.CharField(max_length=100)),
                ('municipality_millage', models.DecimalField(decimal_places=4, max_digits=6)),
                ('municipality_county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.County')),
            ],
        ),
    ]
