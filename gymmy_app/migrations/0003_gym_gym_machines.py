# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymmy_app', '0002_auto_20160506_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='gym_machines',
            field=models.ManyToManyField(to='gymmy_app.GymMachine'),
        ),
    ]
