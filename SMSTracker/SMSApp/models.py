# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField
"""
Model for storage and display of the phone.
"""
class Sms(models.Model):
    from_phone = models.CharField(max_length=20)
    to_phone = models.CharField(max_length=20)
    text = models.TextField(max_length=500, verbose_name=u"Текст",)
    date = models.DateField()
    inbox = models.NullBooleanField(null=True)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User)
    















