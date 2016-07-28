# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalancechange',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 18, 56, 49, 793000)),
        ),
        migrations.AlterField(
            model_name='userbalancechange',
            name='reason',
            field=models.IntegerField(default=b'NR', choices=[(b'SR1', b'SR1'), (b'SR2', b'SR2'), (b'SR3', b'SR3'), (b'NR', b'NR')]),
        ),
    ]
