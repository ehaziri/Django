# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 12:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0003_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
