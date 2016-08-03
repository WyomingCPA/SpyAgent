from django.contrib import admin
from models import GPSCoordinates

class GPSCoordinatesAdmin(admin.ModelAdmin):
    pass

admin.site.register(GPSCoordinates, GPSCoordinatesAdmin)
