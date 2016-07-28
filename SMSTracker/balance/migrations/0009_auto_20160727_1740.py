# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0008_auto_20160723_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalancechange',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 27, 17, 40, 16, 628000)),
        ),
    ]
