from django.contrib import admin
from .models import UserBalanceChange

class UserBalanceChangeAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserBalanceChange, UserBalanceChangeAdmin)
