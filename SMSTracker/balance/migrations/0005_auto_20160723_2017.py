# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0004_auto_20160723_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalancechange',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 23, 20, 17, 34, 597000)),
        ),
    ]
