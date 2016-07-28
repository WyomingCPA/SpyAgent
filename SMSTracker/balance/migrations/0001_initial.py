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
                ('reason', models.IntegerField(default=b'NR', choices=[(b'SR1', b'Freshman'), (b'SR2', b'Sophomore'), (b'SR3', b'Junior'), (b'NR', b'No Reason')])),
                ('amount', models.DecimalField(default=0, max_digits=18, decimal_places=6)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2016, 7, 22, 17, 24, 14, 436000))),
                ('user', models.ForeignKey(related_name='balance_changes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
