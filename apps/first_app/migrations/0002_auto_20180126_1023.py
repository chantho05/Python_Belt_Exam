# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Travel',
        ),
    ]
