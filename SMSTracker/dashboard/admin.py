from django.contrib import admin
from sms_save_app.models import GPSCoordinates

class GPSCoordinatesAdmin(admin.ModelAdmin):
    pass

admin.site.register(GPSCoordinates, GPSCoordinatesAdmin)
