# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0002_auto_20160722_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalancechange',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 19, 2, 56, 586000)),
        ),
        migrations.AlterField(
            model_name='userbalancechange',
            name='reason',
            field=models.IntegerField(default=3, choices=[(0, b'Service1'), (1, b'Service2'), (2, b'Service3'), (3, b'No Reason')]),
        ),
    ]
