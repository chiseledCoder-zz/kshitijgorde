# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-13 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20180107_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]