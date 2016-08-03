from django.db import models
from django.contrib.auth.models import User
from datetime import *

class UserBalanceChange(models.Model):
    SERVICE1 = 'SR1'
    SERVICE2 = 'SR2'
    SERVICE3 = 'SR3'
    NO_REASON = 'NR'
    REASON_CHOICES = (
        (SERVICE1, 'Service1'),
        (SERVICE2, 'Service2'),
        (SERVICE3, 'Service3'),
        (NO_REASON, 'No Reason'),
    )

    user = models.ForeignKey(User, related_name='balance_changes')
    reason = models.CharField(choices=REASON_CHOICES, default=NO_REASON, max_length=7)
    amount = models.DecimalField(default=0, max_digits=18, decimal_places=6)
    datetime = models.DateTimeField(default=datetime.now())
