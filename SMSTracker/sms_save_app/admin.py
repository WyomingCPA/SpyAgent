from django.contrib import admin
from .models import smstel

class SmsTelAdmin(admin.ModelAdmin):
    list_display = ('from_phone', 'to_phone', 'text',)


admin.site.register(smstel, SmsTelAdmin)
