from django.db import models
from django.contrib.auth.models import User
from datetime import *

class UserBalanceChange(models.Model):
    SERVICE1 = 0
    SERVICE2 = 1
    SERVICE3 = 2
    NO_REASON = 3
    REASON_CHOICES = (
        (SERVICE1, 'Service1'),
        (SERVICE2, 'Service2'),
        (SERVICE3, 'Service3'),
        (NO_REASON, 'No Reason'),
    )

    user = models.ForeignKey(User, related_name='balance_changes')
    reason = models.IntegerField(choices=REASON_CHOICES, default=NO_REASON)
    amount = models.DecimalField(default=0, max_digits=18, decimal_places=6)
    datetime = models.DateTimeField(default=datetime.now())
