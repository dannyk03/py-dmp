# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0013_auto_20170525_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataflowsettings',
            name='sync_interval',
            field=models.SmallIntegerField(choices=[(1, '5 minutes'), (2, '30 minutes'), (3, '1 hour'), (4, '2 hours'), (5, '5 hours'), (6, '10 hours'), (7, '24 hours')], default=2),
        ),
    ]
