# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField
"""
Model for storage and display of the phone.
"""
class smstel(models.Model):
    sms_id = models.AutoField(primary_key=True)
    from_phone = models.CharField(max_length=20)
    to_phone = models.CharField(max_length=20)
    text = models.TextField(max_length=500, verbose_name=u"Текст",)
    date = models.DateField()
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User)
    

class GPSCoordinates(models.Model):
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    timestamp = models.DateTimeField()
    geom = PointField()
    user = models.ForeignKey(User, unique=False)



class MoreIdSpy(models.Model):
    """
    The model needs to spy short identifications without login and password
    """
    to_phone = models.CharField(max_length=50, unique = True)
    pin = models.CharField(max_length=10)
    user = models.ForeignKey(User, unique=False)











