# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]