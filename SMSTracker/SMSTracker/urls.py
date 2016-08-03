"""
Definition of urls for SMSTracker.
"""

from django.contrib import admin
from datetime import datetime
from django.conf.urls import url
from django.conf.urls import include
import django.contrib.auth.views
from dashboard.forms import AuthenticationFormCustom, SignupFormCustom

import app.forms
import app.views
import notifications.urls
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from SMSApp.api import SmstelViewSet, UserViewSet
from ToolsApp.api import FindMoreId

router = routers.DefaultRouter()
router.register(r'smstel', SmstelViewSet)
router.register(r'users', UserViewSet)
router.register(r'idspy', FindMoreId)
user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^accounts/inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^accounts/signin/', 'userena.views.signin', { 'auth_form': AuthenticationFormCustom }, name="userena_signin"),
    url(r'^accounts/signup/', 'userena.views.signup', { 'signup_form': SignupFormCustom }, name="userena_signup"),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'userena.views.activate', name='userena_activate'),
    url(r'^accounts/', include('userena.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
