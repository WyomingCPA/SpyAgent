# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField

    
class MoreIdSpy(models.Model):
    """
    The model needs to spy short identifications without login and password
    """
    to_phone = models.CharField(max_length=50, unique = True)
    pin = models.CharField(max_length=10)
    user = models.ForeignKey(User, unique=False)



class SettingsTableSms(models.Model):

    user = models.OneToOneField(User,)
    startDate = models.DateField()
    endsDate = models.DateField()
    text_contains = models.CharField(max_length=200)
    fromphone_contains = models.CharField(max_length=20)
