from .models import MoreIdSpy
from django.contrib.auth.models import User

from rest_framework import serializers

class MoreIdSpySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreIdSpy
        fields = ('to_phone', 'pin', 'user')
