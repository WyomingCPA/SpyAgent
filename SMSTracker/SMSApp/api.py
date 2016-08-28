from .models import Sms
from balance.models import UserBalanceChange
from serializers import SmstelSerializer, UserSerializer
from datetime import datetime

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



class SmstelViewSet(viewsets.ModelViewSet):
    queryset = Sms.objects.all()[0:1]
    serializer_class = SmstelSerializer
    http_method_names = ['post', ]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            check_data = request.data
            try:
                Sms.objects.get(from_phone=check_data['from_phone'], to_phone=check_data['to_phone'], text=check_data['text'], date=check_data['date'], user=check_data['user']) 
            except Sms.DoesNotExist:                
                to_user = User.objects.get(id=check_data['user'])
                sms = Sms(from_phone=check_data['from_phone'], to_phone=check_data['to_phone'], text=check_data['text'], date=check_data['date'], user=to_user, timestamp = datetime.now())          
                sms.save()

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

              
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request):
        """
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
        """
        pk = self.request.user.pk
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)