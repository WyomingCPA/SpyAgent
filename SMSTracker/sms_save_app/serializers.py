from .models import smstel, MoreIdSpy
from django.contrib.auth.models import User

from rest_framework import serializers

class SmstelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = smstel
        #extra_kwargs = {'user': {'default': serializers.CurrentUserDefault()}}
        fields = ('from_phone', 'date', 'timestamp', 'to_phone', 'text', 'user')


class MoreIdSpySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreIdSpy
        fields = ('to_phone', 'pin', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    #mobile = serializers.SerializerMethodField('get_mobile')
    #favourite_locations = serializers.SerializerMethodField('get_favourite_locations')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def get_mobile(self, obj):
        return obj.get_profile().mobile

    def get_favourite_locations(self, obj):
        return obj.get_profile().favourite_locations     