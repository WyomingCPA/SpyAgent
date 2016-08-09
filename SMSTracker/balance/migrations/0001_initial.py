# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBalanceChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(default=b'NR', max_length=7, choices=[(b'SR1', b'Service1'), (b'SR2', b'Service2'), (b'SR3', b'Service3'), (b'NR', b'No Reason')])),
                ('amount', models.DecimalField(default=0, max_digits=18, decimal_places=6)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2016, 8, 9, 23, 40, 51, 307000))),
                ('user', models.ForeignKey(related_name='balance_changes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
