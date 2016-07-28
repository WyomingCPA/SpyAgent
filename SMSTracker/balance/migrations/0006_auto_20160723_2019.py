# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0005_auto_20160723_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalancechange',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 23, 20, 19, 54, 680000)),
        ),
    ]
