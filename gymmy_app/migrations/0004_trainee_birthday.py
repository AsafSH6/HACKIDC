# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymmy_app', '0003_gym_gym_machines'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='birthday',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
