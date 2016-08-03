from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MoreIdSpy
from balance.models import UserBalanceChange
from serializers import MoreIdSpySerializer
from datetime import datetime    


class FindMoreId(viewsets.ModelViewSet):
    queryset = MoreIdSpy.objects.all()
    serializer_class = MoreIdSpySerializer

    def get_queryset(self):
        #to_phone = self.kwargs['to_phone']
        to_phone = self.request.GET['to_phone']
        pin = self.request.GET['pin']
        result = MoreIdSpy.objects.filter(to_phone__contains = to_phone, pin = pin)[0:1]
        return result 

              
         