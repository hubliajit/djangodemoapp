# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-22 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_stock_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='date',
        ),
    ]
