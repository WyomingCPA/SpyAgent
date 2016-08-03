# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField

"""    
class GPSCoordinates(models.Model):
    timestamp = models.DateTimeField()
    geom = PointField()
    user = models.ForeignKey(User, unique=False)
"""



class GPSCoordinates(models.Model):
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    timestamp = models.DateTimeField()
    geom = PointField()
    user = models.ForeignKey(User, unique=False)