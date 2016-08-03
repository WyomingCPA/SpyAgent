from django.contrib import admin
from .models import Sms
class SmsAdmin(admin.ModelAdmin):
    list_display = ('from_phone', 'to_phone', 'text',)

admin.site.register(Sms, SmsAdmin)
