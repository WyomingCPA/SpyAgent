from django.contrib import admin
from .models import SettingsTableSms

class SettingsTableSmsAdmin(admin.ModelAdmin):
    pass


admin.site.register(SettingsTableSms, SettingsTableSmsAdmin)
