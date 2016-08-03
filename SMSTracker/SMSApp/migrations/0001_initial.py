# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_phone', models.CharField(max_length=20)),
                ('to_phone', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=500, verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('date', models.DateField()),
                ('timestamp', models.DateTimeField()),
                ('inbox', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
