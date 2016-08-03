from django.conf.urls import patterns, url, include
from djgeojson.views import GeoJSONLayerView
#from GPSApp.models import GPSCoordinates
from .views import MapLayer

urlpatterns = patterns('',    
    url(r'^$', 'dashboard.views.index', name='index'),
    url(r'^sms/$', 'dashboard.views.sms_table', name='sms_table'),
    url(r'^add_phone/$', 'dashboard.views.add_phone', name='add_phone'),
    url(r'^delete_pointer/$', 'dashboard.views.delete_pointer', name='delete_pointer'),
    url(r'^gps$', 'dashboard.views.gps', name='gps'),
    #url(r'^mushrooms.geojson$', MapLayer.as_view(model=GPSCoordinates, properties=('name',)), name='mushrooms')
   # url(r'^sms/filter/$', 'dashboard.views.sms_table', name='filter'),    
) 